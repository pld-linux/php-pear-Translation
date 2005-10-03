%include	/usr/lib/rpm/macros.php
%define		_class		Translation
%define		_status		stable
%define		_pearname	%{_class}

Summary:	%{_pearname} - class for creating multilingual websites
Summary(pl):	%{_pearname} - klasa do tworzenia wielojêzycznych portali
Name:		php-pear-%{_pearname}
Version:	1.2.6pl1
Release:	2.2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	096296bfe322e4ba250f79bb885ac022
URL:		http://pear.php.net/package/Translation/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-DB
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class allows to store and retrieve all the strings on multilingual
site in the database. Class connects to any database using PHP PEAR
extension. The object should be created for every page. While creation
all the strings connected with specific page and the strings connected
with all the pages on the site are loaded into variable, so access to
them is quite fast and does not overload database server connection.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa ta pozwala na przechowywanie wszystkich ³añcuchów znaków dla
wielojêzycznych serwisów w bazie danych i odczytywanie ich. Klasa
³±czy siê z dowoln± baz± u¿ywaj±c rozszerzenia PHP PEAR. Obiekt mo¿e
byæ tworzony dla ka¿dej strony. Od utworzenia wszystkie ³añcuchy
powi±zane z dan± stron±, a tak¿e ³añcuchy powi±zane ze wszystkimi
stronami z serwisu s± wczytywane do zmiennej, wiêc dostêp do nich jest
szybki i nie przeci±¿a po³±czenia z serwerem baz danych.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
