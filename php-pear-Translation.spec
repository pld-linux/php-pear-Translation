%include	/usr/lib/rpm/macros.php
%define		_class		Translation
%define		_pearname	%{_class}
Summary:	%{_pearname} - class for creating multilingual websites
Summary(pl):	%{_pearname} - klasa do tworzenia wielojêzycznych portali
Name:		php-pear-%{_pearname}
Version:	1.2
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class allows to store and retrieve all the strings on multilingual
site in the database. Class connects to any database using PHP PEAR
extension. The object should be created for every page. While creation
all the strings connected with specific page and the strings connected
with all the pages on the site are loaded into variable, so access to
them is quite fast and does not overload database server connection.

%description -l pl
Klasa ta pozwala na przechowywanie wszystkich ³añcuchów znaków dla
wielojêzycznych serwisów w bazie danych i odczytywanie ich. Klasa
³±czy siê z dowoln± baz± u¿ywaj±c rozszerzenia PHP PEAR. Obiekt mo¿e
byæ tworzony dla ka¿dej strony. Od utworzenia wszystkie ³añcuchy
powi±zane z dan± stron±, a tak¿e ³añcuchy powi±zane ze wszystkimi
stronami z serwisu s± wczytywane do zmiennej, wiêc dostêp do nich
jest szybki i nie przeci±¿a po³±czenia z serwerem baz danych.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/doc/*
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/%{_class}/*.php
