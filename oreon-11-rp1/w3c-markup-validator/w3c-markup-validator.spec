%global source0_hash c3c0febbf3ed0c628168e1ad937f0cc984a16e0bfafb6f2e9c9e969decba0160
%global __requires_exclude perl\\(W3C::Validator::EventHandler\\)
Name:           w3c-markup-validator
Version:        1.3
Release:        32%{?dist}
Summary:        W3C Markup Validator
License:        W3C
URL:            http://validator.w3.org/
Source0:        %{name}-%{version}.tar.xz
Source99:       %{name}-prepare-tarball.sh
Patch0:         %{name}-1.2-config.patch
Patch1:         %{name}-1.3-syspaths.patch
Patch2:         %{name}-1.0-valid-icons.patch
Patch3:         %{name}-1.3-iso-html.patch
Patch4:         %{name}-apache24.patch
BuildArch:      noarch
Requires:       httpd
Requires:       %{name}-libs = %{version}
Requires:       perl(XML::LibXML) >= 1.70
Recommends:       perl(HTML::Tidy)
# oreon:deps
BuildRequires:  /usr/bin/perl
BuildRequires:  perl-generators
# /oreon:deps
%description
The W3C Markup Validator checks documents like HTML and XHTML for
conformance to W3C Recommendations and other standards.

%package        libs
Summary:        SGML and XML DTDs for the W3C Markup Validator
Requires:       sgml-common
Requires:       html401-dtds
Requires:       xhtml1-dtds >= 1.0-20020801.1
%description    libs
SGML and XML DTDs for the W3C Markup Validator.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n validator-%{version}

# Remove not needed stuff
rm -r htdocs/sgml-lib/REC-html401-19991224
rm -r htdocs/sgml-lib/REC-xhtml1-20020801
rm htdocs/images/markup_validation_service.psd

%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

find . -type f -name "*.orig" -delete # patch backup files

mv htdocs/sgml-lib .

# Localize configs.
%{__perl} -pi -e \
  's|/usr/local/validator\b|%{_datadir}/%{name}|' \
  htdocs/config/validator.conf httpd/conf/httpd.conf httpd/cgi-bin/*
%{__perl} -pi -e \
  's|\$Base/htdocs/sgml-lib|%{_datadir}/sgml/%{name}| ;
   s|\$Base/htdocs/config/tidy\.conf|%{_sysconfdir}/w3c/tidy.conf|' \
  htdocs/config/validator.conf
%{__perl} -pi -e \
  's|\$home/htdocs/sgml-lib/catalog\.xml|%{_datadir}/sgml/%{name}/catalog.xml|' \
  httpd/mod_perl/startup.pl

# Move config out of the way
mv htdocs/config __config

%build

%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/w3c
install -pm 644 __config/* $RPM_BUILD_ROOT%{_sysconfdir}/w3c
install -Dpm 644 httpd/conf/httpd.conf \
  $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/%{name}.conf
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/httpd
cp -pR httpd/cgi-bin htdocs share $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pR httpd/mod_perl $RPM_BUILD_ROOT%{_datadir}/%{name}/httpd
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/sgml
cp -pR sgml-lib $RPM_BUILD_ROOT%{_datadir}/sgml/%{name}
ln -s ../html/4.01 $RPM_BUILD_ROOT%{_datadir}/sgml/%{name}/REC-html401-19991224
ln -s ../../xml/xhtml/1.0 \
  $RPM_BUILD_ROOT%{_datadir}/sgml/%{name}/REC-xhtml1-20020801
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/sgml
touch $RPM_BUILD_ROOT%{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

[ $1 -eq 1 ] && systemctl reload httpd || :
%postun

%systemd_postun_with_restart httpd
%post libs

for catalog in sgml.soc xml.soc ; do
  install-catalog --add \
    %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat \
    %{_datadir}/sgml/%{name}/$catalog >/dev/null 2>&1 || :
done
%preun libs

for catalog in sgml.soc xml.soc ; do
  install-catalog --remove \
    %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat \
    %{_datadir}/sgml/%{name}/$catalog >/dev/null 2>&1 || :
done
%files -f %{oreon_filedir}/main.list
%files -n w3c-markup-validator-libs -f %{oreon_filedir}/w3c-markup-validator-libs.list

%changelog

%autochangelog
