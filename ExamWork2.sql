PGDMP                         }        
   ExamPaper2    12.22    12.22 #    -           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            .           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            /           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            0           1262    16394 
   ExamPaper2    DATABASE     �   CREATE DATABASE "ExamPaper2" WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'English_United Kingdom.1252' LC_CTYPE = 'English_United Kingdom.1252';
    DROP DATABASE "ExamPaper2";
                postgres    false            �            1259    16410    Account_Details    TABLE     �   CREATE TABLE public."Account_Details" (
    "Account_ID" integer NOT NULL,
    "Username" character varying(100) NOT NULL,
    "Password" character varying(100) NOT NULL,
    "User_ID" integer NOT NULL
);
 %   DROP TABLE public."Account_Details";
       public         heap    postgres    false            �            1259    16408    Account_Details_Account_ID_seq    SEQUENCE     �   CREATE SEQUENCE public."Account_Details_Account_ID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 7   DROP SEQUENCE public."Account_Details_Account_ID_seq";
       public          postgres    false    205            1           0    0    Account_Details_Account_ID_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public."Account_Details_Account_ID_seq" OWNED BY public."Account_Details"."Account_ID";
          public          postgres    false    204            �            1259    16447    Consultations    TABLE     �   CREATE TABLE public."Consultations" (
    "Consultation_ID" integer NOT NULL,
    "Consult_Date" date,
    "Topic" text,
    "Phone" text,
    "Address" text
);
 #   DROP TABLE public."Consultations";
       public         heap    postgres    false            �            1259    16445 !   Consultations_Consultation_ID_seq    SEQUENCE     �   CREATE SEQUENCE public."Consultations_Consultation_ID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 :   DROP SEQUENCE public."Consultations_Consultation_ID_seq";
       public          postgres    false    209            2           0    0 !   Consultations_Consultation_ID_seq    SEQUENCE OWNED BY     m   ALTER SEQUENCE public."Consultations_Consultation_ID_seq" OWNED BY public."Consultations"."Consultation_ID";
          public          postgres    false    208            �            1259    16436    Installations    TABLE     �   CREATE TABLE public."Installations" (
    "Booking_ID" integer NOT NULL,
    "Install_Date" date,
    "Product" text,
    "Phone" text,
    "Address" text
);
 #   DROP TABLE public."Installations";
       public         heap    postgres    false            �            1259    16434    Installations_Booking_ID_seq    SEQUENCE     �   CREATE SEQUENCE public."Installations_Booking_ID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 5   DROP SEQUENCE public."Installations_Booking_ID_seq";
       public          postgres    false    207            3           0    0    Installations_Booking_ID_seq    SEQUENCE OWNED BY     c   ALTER SEQUENCE public."Installations_Booking_ID_seq" OWNED BY public."Installations"."Booking_ID";
          public          postgres    false    206            �            1259    16397    User_Details    TABLE        CREATE TABLE public."User_Details" (
    "User_ID" integer NOT NULL,
    "Forename" character varying(100) NOT NULL,
    "Surname" character varying(100) NOT NULL,
    "Email" character varying(100) NOT NULL,
    "Address" text NOT NULL,
    "Post_code" character varying(20) NOT NULL
);
 "   DROP TABLE public."User_Details";
       public         heap    postgres    false            �            1259    16395    User_Details_User_ID_seq    SEQUENCE     �   CREATE SEQUENCE public."User_Details_User_ID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public."User_Details_User_ID_seq";
       public          postgres    false    203            4           0    0    User_Details_User_ID_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public."User_Details_User_ID_seq" OWNED BY public."User_Details"."User_ID";
          public          postgres    false    202            �
           2604    16413    Account_Details Account_ID    DEFAULT     �   ALTER TABLE ONLY public."Account_Details" ALTER COLUMN "Account_ID" SET DEFAULT nextval('public."Account_Details_Account_ID_seq"'::regclass);
 M   ALTER TABLE public."Account_Details" ALTER COLUMN "Account_ID" DROP DEFAULT;
       public          postgres    false    204    205    205            �
           2604    16450    Consultations Consultation_ID    DEFAULT     �   ALTER TABLE ONLY public."Consultations" ALTER COLUMN "Consultation_ID" SET DEFAULT nextval('public."Consultations_Consultation_ID_seq"'::regclass);
 P   ALTER TABLE public."Consultations" ALTER COLUMN "Consultation_ID" DROP DEFAULT;
       public          postgres    false    209    208    209            �
           2604    16439    Installations Booking_ID    DEFAULT     �   ALTER TABLE ONLY public."Installations" ALTER COLUMN "Booking_ID" SET DEFAULT nextval('public."Installations_Booking_ID_seq"'::regclass);
 K   ALTER TABLE public."Installations" ALTER COLUMN "Booking_ID" DROP DEFAULT;
       public          postgres    false    207    206    207            �
           2604    16400    User_Details User_ID    DEFAULT     �   ALTER TABLE ONLY public."User_Details" ALTER COLUMN "User_ID" SET DEFAULT nextval('public."User_Details_User_ID_seq"'::regclass);
 G   ALTER TABLE public."User_Details" ALTER COLUMN "User_ID" DROP DEFAULT;
       public          postgres    false    202    203    203            &          0    16410    Account_Details 
   TABLE DATA           \   COPY public."Account_Details" ("Account_ID", "Username", "Password", "User_ID") FROM stdin;
    public          postgres    false    205   +       *          0    16447    Consultations 
   TABLE DATA           i   COPY public."Consultations" ("Consultation_ID", "Consult_Date", "Topic", "Phone", "Address") FROM stdin;
    public          postgres    false    209   0+       (          0    16436    Installations 
   TABLE DATA           f   COPY public."Installations" ("Booking_ID", "Install_Date", "Product", "Phone", "Address") FROM stdin;
    public          postgres    false    207   �+       $          0    16397    User_Details 
   TABLE DATA           k   COPY public."User_Details" ("User_ID", "Forename", "Surname", "Email", "Address", "Post_code") FROM stdin;
    public          postgres    false    203   �+       5           0    0    Account_Details_Account_ID_seq    SEQUENCE SET     N   SELECT pg_catalog.setval('public."Account_Details_Account_ID_seq"', 1, true);
          public          postgres    false    204            6           0    0 !   Consultations_Consultation_ID_seq    SEQUENCE SET     Q   SELECT pg_catalog.setval('public."Consultations_Consultation_ID_seq"', 1, true);
          public          postgres    false    208            7           0    0    Installations_Booking_ID_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public."Installations_Booking_ID_seq"', 2, true);
          public          postgres    false    206            8           0    0    User_Details_User_ID_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public."User_Details_User_ID_seq"', 1, true);
          public          postgres    false    202            �
           2606    16417 ,   Account_Details Account_Details_Username_key 
   CONSTRAINT     q   ALTER TABLE ONLY public."Account_Details"
    ADD CONSTRAINT "Account_Details_Username_key" UNIQUE ("Username");
 Z   ALTER TABLE ONLY public."Account_Details" DROP CONSTRAINT "Account_Details_Username_key";
       public            postgres    false    205            �
           2606    16415 $   Account_Details Account_Details_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public."Account_Details"
    ADD CONSTRAINT "Account_Details_pkey" PRIMARY KEY ("Account_ID");
 R   ALTER TABLE ONLY public."Account_Details" DROP CONSTRAINT "Account_Details_pkey";
       public            postgres    false    205            �
           2606    16455     Consultations Consultations_pkey 
   CONSTRAINT     q   ALTER TABLE ONLY public."Consultations"
    ADD CONSTRAINT "Consultations_pkey" PRIMARY KEY ("Consultation_ID");
 N   ALTER TABLE ONLY public."Consultations" DROP CONSTRAINT "Consultations_pkey";
       public            postgres    false    209            �
           2606    16444     Installations Installations_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public."Installations"
    ADD CONSTRAINT "Installations_pkey" PRIMARY KEY ("Booking_ID");
 N   ALTER TABLE ONLY public."Installations" DROP CONSTRAINT "Installations_pkey";
       public            postgres    false    207            �
           2606    16407 #   User_Details User_Details_Email_key 
   CONSTRAINT     e   ALTER TABLE ONLY public."User_Details"
    ADD CONSTRAINT "User_Details_Email_key" UNIQUE ("Email");
 Q   ALTER TABLE ONLY public."User_Details" DROP CONSTRAINT "User_Details_Email_key";
       public            postgres    false    203            �
           2606    16405    User_Details User_Details_pkey 
   CONSTRAINT     g   ALTER TABLE ONLY public."User_Details"
    ADD CONSTRAINT "User_Details_pkey" PRIMARY KEY ("User_ID");
 L   ALTER TABLE ONLY public."User_Details" DROP CONSTRAINT "User_Details_pkey";
       public            postgres    false    203            �
           2606    16418 ,   Account_Details Account_Details_User_ID_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Account_Details"
    ADD CONSTRAINT "Account_Details_User_ID_fkey" FOREIGN KEY ("User_ID") REFERENCES public."User_Details"("User_ID") ON DELETE CASCADE;
 Z   ALTER TABLE ONLY public."Account_Details" DROP CONSTRAINT "Account_Details_User_ID_fkey";
       public          postgres    false    205    2715    203            &      x�3��sq�r��~��\1z\\\ F<      *   F   x�3�4202�50�5��t�K-J�T(N,��KW(�,(�407�0450132���M-�H-JU(J����� �      (   O   x�3�4202�50�52���I,RH�K�)�407�0450132 J䦖g��*�pA�����R��������� �2�      $   @   x�3��K,�t�/J����K,I��s3s���s9��sS�3R�R�R8�S�L+�b���� sL_     