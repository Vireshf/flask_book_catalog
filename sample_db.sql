PGDMP         #        	        x            sample    11.8    11.8                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false                       1262    16393    sample    DATABASE     �   CREATE DATABASE sample WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'English_United States.1252' LC_CTYPE = 'English_United States.1252';
    DROP DATABASE sample;
             postgres    false            �            1259    16412    book    TABLE     ;  CREATE TABLE public.book (
    id integer NOT NULL,
    title character varying(80) NOT NULL,
    author character varying(80),
    avg_rating double precision,
    format character varying(80),
    image character varying(80),
    num_pages integer,
    pub_date timestamp without time zone,
    pub_id integer
);
    DROP TABLE public.book;
       public         postgres    false            �            1259    16410    book_id_seq    SEQUENCE     �   CREATE SEQUENCE public.book_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 "   DROP SEQUENCE public.book_id_seq;
       public       postgres    false    199                       0    0    book_id_seq    SEQUENCE OWNED BY     ;   ALTER SEQUENCE public.book_id_seq OWNED BY public.book.id;
            public       postgres    false    198            �            1259    16404    publication    TABLE     f   CREATE TABLE public.publication (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);
    DROP TABLE public.publication;
       public         postgres    false            �            1259    16402    publication_id_seq    SEQUENCE     �   CREATE SEQUENCE public.publication_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.publication_id_seq;
       public       postgres    false    197                       0    0    publication_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.publication_id_seq OWNED BY public.publication.id;
            public       postgres    false    196            �            1259    16462    users    TABLE     �   CREATE TABLE public.users (
    id integer NOT NULL,
    user_name character varying(80) NOT NULL,
    user_email character varying(80) NOT NULL,
    user_password character varying(80) NOT NULL,
    registration_date timestamp without time zone
);
    DROP TABLE public.users;
       public         postgres    false            �            1259    16460    users_id_seq    SEQUENCE     �   CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.users_id_seq;
       public       postgres    false    201                       0    0    users_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;
            public       postgres    false    200            �
           2604    16415    book id    DEFAULT     b   ALTER TABLE ONLY public.book ALTER COLUMN id SET DEFAULT nextval('public.book_id_seq'::regclass);
 6   ALTER TABLE public.book ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    199    198    199            �
           2604    16407    publication id    DEFAULT     p   ALTER TABLE ONLY public.publication ALTER COLUMN id SET DEFAULT nextval('public.publication_id_seq'::regclass);
 =   ALTER TABLE public.publication ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    197    196    197            �
           2604    16465    users id    DEFAULT     d   ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);
 7   ALTER TABLE public.users ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    200    201    201                      0    16412    book 
   TABLE DATA               i   COPY public.book (id, title, author, avg_rating, format, image, num_pages, pub_date, pub_id) FROM stdin;
    public       postgres    false    199                    0    16404    publication 
   TABLE DATA               /   COPY public.publication (id, name) FROM stdin;
    public       postgres    false    197   �                 0    16462    users 
   TABLE DATA               \   COPY public.users (id, user_name, user_email, user_password, registration_date) FROM stdin;
    public       postgres    false    201   p                  0    0    book_id_seq    SEQUENCE SET     9   SELECT pg_catalog.setval('public.book_id_seq', 6, true);
            public       postgres    false    198                        0    0    publication_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.publication_id_seq', 6, true);
            public       postgres    false    196            !           0    0    users_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.users_id_seq', 4, true);
            public       postgres    false    200            �
           2606    16419    book book_image_key 
   CONSTRAINT     O   ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_image_key UNIQUE (image);
 =   ALTER TABLE ONLY public.book DROP CONSTRAINT book_image_key;
       public         postgres    false    199            �
           2606    16417    book book_pkey 
   CONSTRAINT     L   ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_pkey PRIMARY KEY (id);
 8   ALTER TABLE ONLY public.book DROP CONSTRAINT book_pkey;
       public         postgres    false    199            �
           2606    16409    publication publication_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.publication
    ADD CONSTRAINT publication_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.publication DROP CONSTRAINT publication_pkey;
       public         postgres    false    197            �
           2606    16467    users users_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public         postgres    false    201            �
           1259    16425    ix_book_title    INDEX     ?   CREATE INDEX ix_book_title ON public.book USING btree (title);
 !   DROP INDEX public.ix_book_title;
       public         postgres    false    199            �
           1259    16468    ix_users_user_email    INDEX     R   CREATE UNIQUE INDEX ix_users_user_email ON public.users USING btree (user_email);
 '   DROP INDEX public.ix_users_user_email;
       public         postgres    false    201            �
           2606    16420    book book_pub_id_fkey    FK CONSTRAINT     y   ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_pub_id_fkey FOREIGN KEY (pub_id) REFERENCES public.publication(id);
 ?   ALTER TABLE ONLY public.book DROP CONSTRAINT book_pub_id_fkey;
       public       postgres    false    197    2701    199               �   x�}ϱ�!���� �1�ژ�Z��lcC"8.���w2��1����=y_��[ﲯ�#<����3]�Z�0%���Ϡ��=�V��y���:[�l
����&4H���n���fl4D�:�?{�fX�6G_�����8B��?�d�;-pr����W\�M8�jǷR��wπi����ҝI��6�|�~_�'��%�V         g   x�MȻ�0 �Z�BP�� t�� i����lH�%�k��Ib������+��I-Q8��I�`��0�%Ӡ�vzH�f���Iٲy�?|v��C$�         I  x�e��n�P�5<���q@V�5ڊ��t�~קom�����̿�|��6*���&n�,��B4��c�_7�<YϜ�E�-�5�%���3p��R\�Zs]t�I	� #@G@@�@� Y ��0�W���<Z^@�>2w����@�l���+lȥ9�f{+j���Fz����D� � �J����ΥI���xT�0��j�J�&)E��ƯѾ!���f`O�[}\0��ju��$s�$���*V�$�	�'�'�*���n]�yS~�G9hw�:)�}�KOo��Q��꺔i�N���E���Z��m���V@YADAX !�o��Oh��     