%include	/usr/lib/rpm/macros.php
%define		_class		Structures
%define		_subclass	DataGrid_DataSource_Array
%define		_status		beta
%define		_pearname	Structures_DataGrid_DataSource_Array
Summary:	%{_pearname} - DataSource driver using arrays
Summary(pl.UTF-8):	%{_pearname} - sterownik DataSource dla tablic
Name:		php-pear-%{_pearname}
Version:	0.1.2
Release:	2
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	ddf4856f27390eca734bd10fb92188d0
URL:		http://pear.php.net/package/Structures_DataGrid_DataSource_Array/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.4.9
Requires:	php-pear-Structures_DataGrid >= 0.7.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a DataSource driver for Structures_DataGrid using arrays. It
is a base package for some other DataSource drivers like CSV or XML.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten pakiet dostarcza sterownik DataSource do tablic dla
Structures_DataGrid. Jest to klasa bazowa dla innych sterowników
DataSource, takich jak CSV czy XML.

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
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Structures/DataGrid/DataSource/Array.php
