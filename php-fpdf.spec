Summary:	PHP class to generate PDF files
Name:		php-fpdf
Version:	1.6
Release:	%mkrel 4
License:	MIT
Group:		Development/PHP
Source0:	fpdf16.tgz
URL:		http://www.fpdf.org

BuildArch:	noarch
BuildRequires:	dos2unix

BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
FPDF is a PHP class that allow generating PDF files with pure PHP, that is to
say without using the PDFlib library. FPDF provides high-level functions and 
has the following main features:

 - Choice of measure unit, page format, and margins
 - Page header and footer management
 - Automatic page break
 - Automatic line break and text justification
 - Image support (JPEG and PNG)
 - Colors
 - Links
 - TrueType, Type1, and encoding support
 - Page compression

%prep

%setup -q -n fpdf16

find . -name "*.htm" \
     -name "*.css" \
     -name "*.txt" \
     -name "*.ini" \
     -name "*.mat" \
     -name "*.afm" \
     -name "*.ttf" \
     -name "*.z" \
     -name "*.png" \
     -exec chmod 644 {} \;

find . -name "*.txt" -name "*.ini" -exec dos2unix -U {} \;

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/php/fpdf
cp -a fpdf.php %{buildroot}%{_datadir}/php/fpdf/
cp -pR font %{buildroot}%{_datadir}/php/fpdf/

install -d %{buildroot}%{_docdir}/php-fpdf
cp -pR doc %{buildroot}%{_docdir}/php-fpdf/
cp -pR tutorial %{buildroot}%{_docdir}/php-fpdf/
cp -p FAQ.htm fpdf.css fpdf.php histo.htm install.txt license.txt %{buildroot}%{_docdir}/php-fpdf/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%{_datadir}/php/fpdf
%{_docdir}/php-fpdf

