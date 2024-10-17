Summary:	PHP class to generate PDF files
Name:		php-fpdf
Version:	1.6
Release:	7
License:	MIT
Group:		Development/PHP
Source0:	fpdf16.tgz
URL:		https://www.fpdf.org

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

find . -name "*.txt" -name "*.ini" -exec dos2unix {} \;

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



%changelog
* Sun Jan 15 2012 Oden Eriksson <oeriksson@mandriva.com> 1.6-6mdv2012.0
+ Revision: 761227
- rebuild

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.6-5
+ Revision: 679255
- mass rebuild

* Sat Jan 08 2011 Oden Eriksson <oeriksson@mandriva.com> 1.6-4mdv2011.0
+ Revision: 629790
- rebuilt for php-5.3.5

* Sun Oct 24 2010 Oden Eriksson <oeriksson@mandriva.com> 1.6-3mdv2011.0
+ Revision: 588792
- rebuild

* Sat Jan 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1.6-2mdv2010.1
+ Revision: 485358
- rebuilt for php-5.3.2RC1

* Wed Sep 02 2009 Stéphane Téletchéa <steletch@mandriva.org> 1.6-1mdv2010.0
+ Revision: 424070
- Initial Mandriva release


* Tue Sep 1 2009 Stéphane Téletchéa <steletch@mandriva.org> - 1.6-1mdv2010.0
- Initial package for Mandriva
