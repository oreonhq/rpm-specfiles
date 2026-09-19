%global source0_hash fe042e9fcc34b77cb6c008090257a25c39e3c1f5e3b0cac99e4eef142954fe70

%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%global pear_name HTML_Template_IT

Name:           php-pear-HTML-Template-IT
Version:        1.3.0
Release:        32%{?dist}
Summary:        Integrated Templates

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://pear.php.net/package/HTML_Template_IT
Source0:        http://download.pear.php.net/package/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  php-pear

Requires(post): %{__pear}
Requires(postun): %{__pear}
# from phpcompatinfo report
Requires:       php-pcre
Requires:       php-pear(PEAR)

Provides:       php-pear(%{pear_name}) = %{version}

%description
HTML_Template_IT:
The Isotemplate API is somewhat tricky for a beginner although it is the
best one you can build.

Source and target can be block names or even handler names. This API gives
you a maximum of flexibility but you always have to know what you do which 
is quite unusual for php developer like me.
If all blocks are within one file, the script knows how they are nested and
in which way you have to parse them. IT knows that inner1 is a child of
block2, there's no need to tell him about this.

Features :
  * Nested blocks
  * Include external file
  * Custom tags format 

HTML_Template_ITX :
With this class you get the full power of the php lib template class.
You may have one file with blocks in it but you have as well one main file
and multiple files one for each block. This is quite useful when you have
user configurable websites. Using blocks not in the main template allows
you to modify some parts of your layout easily.

 
%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
cd %{pear_name}-%{version}
mv ../package.xml %{name}.xml

%build
cd %{pear_name}-%{version}
# Empty build section, most likely nothing required.

%install
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot $RPM_BUILD_ROOT %{name}.xml

# Clean up unnecessary files
rm -rf $RPM_BUILD_ROOT%{pear_metadir}/.??*

# Install XML package description
mkdir -p $RPM_BUILD_ROOT%{pear_xmldir}
install -pm 644 %{name}.xml $RPM_BUILD_ROOT%{pear_xmldir}

# fix wrong-file-end-of-line-encoding
sed -e 's/\r//' -i \
    $RPM_BUILD_ROOT%{pear_docdir}/%{pear_name}/LICENSE \
    $RPM_BUILD_ROOT%{pear_docdir}/%{pear_name}/examples/*.php

%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        pear.php.net/%{pear_name} >/dev/null || :
fi

%files
%doc %{pear_docdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%dir %{pear_phpdir}/HTML
%dir %{pear_phpdir}/HTML/Template
%{pear_phpdir}/HTML/Template/IT.php
%{pear_phpdir}/HTML/Template/ITX.php
%{pear_phpdir}/HTML/Template/IT_Error.php
%{pear_testdir}/%{pear_name}

%changelog
%autochangelog
