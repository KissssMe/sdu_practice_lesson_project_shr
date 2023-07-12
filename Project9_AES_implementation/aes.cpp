#include <iostream>
#include <chrono>
#include <time.h>

using namespace std;
//�л�Ͼ���
char encry_s[4][4] = {
	{0x02,0x03,0x01,0x01},
	{0x01,0x02,0x03,0x01},
	{0x01,0x01,0x02,0x03},
	{0x03,0x01,0x01,0x02}
};
//s��
char S_Box[16][16] = {
	{0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76},
	{0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0},
	{0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15},
	{0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75},
	{0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84},
	{0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF},
	{0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8},
	{0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2},
	{0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73},
	{0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB},
	{0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79},
	{0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08},
	{0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A},
	{0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E},
	{0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF},
	{0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16}
};

//��亯������Ϊ128λ
void padded(const char* input,int input_len,char* output){
	int padding_len = 16 - input_len;
	memcpy(output, input, input_len);
	memset(output + input_len, '0', padding_len);
}
//�����
void XOR(char* a, char* b) {
	for (int i = 0; i < 4; i++) {
		a[i] = a[i] ^ b[i];
	}
}

//��s���滻
void sbox_sub(char*m){
	for (int i = 0; i < 16; i++) {
		int value = (int)m[i];
		int high = (value >> 4) & 0x0f; // ��ȡ����λ
		int low = value & 0x0f; // ��ȡ����λ
		m[i] = S_Box[high][low];
	}
}
//����λ
void row_shift(char* m) {
	//�ڶ���
	char tmp = m[1];
	for (int i = 1; i <= 9; i += 4) {
		m[i] = m[(i + 4) % 16];
	}
	m[13] = tmp;
	//������
	swap(m[2], m[10]);
	swap(m[6], m[14]);
	//������
	tmp = m[15];
	for (int i = 15; i >= 7; i -= 4) {
		m[i] = m[(i - 4)];
	}
	m[3] = tmp;
}
//�л���еĳ˷�
char MulInMix(char a, char b) {
	char output;
	char output_tmp;
	//�ж�b��λ�Ƿ�Ϊ0
	char flag = 0x80;
	flag = flag & b;
	if (flag == 0x00) {    //��λΪ0ֱ����λ
		output_tmp = b << 1;
	}
	else {		//��λ��Ϊ0��λ�����0x1b
		output_tmp = (b << 1) ^ 0x1b;
	}
	if (a == 0x01)
		output = b;		//��������
	else if (a == 0x02) {
		output = output_tmp;
	}
	else
		output = output_tmp ^ b;
	return output;
}
//�л��*
void col_mix(char* m) {
	char m_tmp[16] = {};
	for (int i = 0; i < 16; i++) {
		char tmp;
		int col = i / 4;//����
		int row = i % 4;//����
		tmp = MulInMix(encry_s[row][0], m[4 * col]);
		for (int j = 1; j < 4; j++) {
			tmp ^= MulInMix(encry_s[row][j], m[4 * col + j]);
		}
		m_tmp[i] = tmp;
	}
	for (int i = 0; i < 16; i++) {
		m[i] = m_tmp[i];
	}
}
//��Կ��չ
//�ֳ���
char rcon[10] = {
0x01, 0x02, 0x04, 0x08, 0x10,
0x20, 0x40, 0x80, 0x1B, 0x36
};

//4λs���滻
void sbox_sub_4(char* m) {
	for (int i = 0; i < 4; i++) {
		int value = (int)m[i];
		int high = (value >> 4) & 0x0f; // ��ȡ����λ
		int low = value & 0x0f; // ��ȡ����λ
		m[i] = S_Box[high][low];
	}
}
//4λ��λ
char* shift_4bit(char* w) {
	char *w0=new char[4];
	for (int i = 0; i < 4; i++) {
		w0[i] = w[i];	//��ֵ���Ƶ�һ����������
	}
	char tmp = w0[0];
	for (int i = 0; i < 3; i++) {
		w0[i] = w0[i + 1];	  //����һλ�⣬������λ��ֵ
	}
	w0[3] = tmp;
	return w0;
}
//T����
char* T(char* w,int a) {
	char* tmp = new char[4];
	tmp=shift_4bit(w);
	sbox_sub_4(tmp);
	tmp[0] = tmp[0] ^ rcon[a];
	for (int i = 1; i <= 3; i++) {
		tmp[i] = tmp[i] ^ 0x00;
	}
	return tmp;
}
//��Կ��չ����
void key_wide(char* key_0,char (*key)[4]) {
	//for (int i = 0; i < 4; i++) {
		//key[i] = key_0 + 4 * i;
	//}
	for (int i = 0; i < 4; i++) {
		memcpy(key[i], key_0 + 4 * i, sizeof(char) * 4);
	}
	for (int i = 4; i <= 43; i++) {
		if (i % 4 == 0) {
			for (int j = 0; j < 4; j++) {
				key[i][j] = T(key[i - 1], i / 4 - 1)[j] ^ key[i - 4][j];
			}
		}
		else {
			for (int j = 0; j < 4; j++) {
				key[i][j] = key[i - 1][j] ^ key[i - 4][j];
			}
		}
	}
}

void aes128(char* m_0, char* k_0) {
	cout << endl << "����Ϊ";
	for (int i = 0; i < 12; i++) {
		printf("%02x ", (unsigned char)m_0[i]);
	}
	/*cout << endl << "��ԿΪ" ;
	for (int i = 0; i < 12; i++) {
		printf("%02x ", (unsigned char)k_0[i]);
	}*/
	char m[16];
	char k[16];

	//������ĺ���Կ
	padded(m_0, 12, m);
	padded(k_0, 12, k);
	char* c = m;
	//��������Կ
	char key[44][4] = {};
	key_wide(k, key);
	//�����Կ
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			m[i * 4 + j] ^= key[i][j];
		}
	}
	//�ظ�9�ֲ���
	for (int i = 0; i < 9; i++) {
		sbox_sub(m);
		row_shift(m);
		col_mix(m);
		for (int z = 0; z < 4; z++) {
			for (int j = 0; j < 4; j++) {
				m[z * 4 + j] ^= key[4 + 4 * i + z][j];
			}
		}
	}
	sbox_sub(m);
	row_shift(m);
	//���һ��Ϊ����Կ��
	for (int z = 0; z < 4; z++) {
		for (int j = 0; j < 4; j++) {
			m[z * 4 + j] ^= key[40 + z][j];
		}
	}
	cout << endl << "���ܺ������Ϊ��";
	for (int i = 0; i < 16; i++) {
		printf("%02x ", (unsigned char)m[i]);
	}
}

int main() {
	char m_0[16] = "202100460085";
	char k_0[16] = "202100460085";
	aes128(m_0, k_0);
	return 0;
}
