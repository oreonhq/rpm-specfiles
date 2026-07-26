%global source0_hash 046487f084c12fa1c822affc5f7de56efed9b48905a426e631a6b949c114d86c

%{!?_httpd_apxs: %{expand: %%global _httpd_apxs %%{_sbindir}/apxs}}
%{!?_httpd_mmn: %{expand: %%global _httpd_mmn %%(cat %{_includedir}/httpd/.mmn || echo 0-0)}}
%{!?_httpd_confdir:    %{expand: %%global _httpd_confdir    %%{_sysconfdir}/httpd/conf.d}}
# /etc/httpd/conf.d with httpd < 2.4 and defined as /etc/httpd/conf.modules.d with httpd >= 2.4
%{!?_httpd_modconfdir: %{expand: %%global _httpd_modconfdir %%{_sysconfdir}/httpd/conf.d}}

Name:           libapreq2
Version:        2.17
Release:        14%{?dist}
Summary:        Apache HTTP request library

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://httpd.apache.org/apreq/
Source0:        http://www.apache.org/dist/httpd/libapreq/libapreq2-%{version}.tar.gz
Source1:        %{name}-httpd.conf
Source2:        %{name}.pc.in
Patch0:         %{name}-build.patch
Patch1:         %{name}-2.07-rc3-ldflags.patch
Patch2:         %{name}-2.09-pkgconfig.patch
Patch3:         %{name}-2.12-install.patch
Patch4:         %{name}-2.17-incompatible-pointer.patch

BuildRequires:  httpd-devel >= 2.0.48
BuildRequires:  libtool
BuildRequires:  apr-devel >= 0.9.4
BuildRequires:  apr-util-devel >= 0.9.4
BuildRequires:  perl(ExtUtils::XSBuilder)
BuildRequires:  perl(Apache::Test)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  mod_perl-devel >= 2.0.0-0.rc5
BuildRequires: make
BuildRequires: libxcrypt-devel
Requires:       httpd-mmn = %{_httpd_mmn}
Provides:       libapreq = %{version}-%{release}

%description
libapreq is a shared library with associated modules for manipulating
client request data via the Apache API.  Functionality includes
parsing of application/x-www-form-urlencoded and multipart/form-data
content, as well as HTTP cookies.

%package        libs
Summary:        Libraries for %{name}
Provides:       libapreq-libs = %{version}-%{release}

%description    libs
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       httpd-devel >= 2.0.48
Requires:       pkgconfig
Provides:       libapreq-devel = %{version}-%{release}

%description    devel
%{summary}.

%package     -n perl-%{name}
Summary:        Perl interface to the Apache HTTP request library
Requires:       mod_perl >= 2.0.0-0.rc5
Provides:       perl-libapreq = %{version}-%{release}

%description -n perl-%{name}
This package contains a Perl interface to the Apache HTTP request
library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# Filter unversioned provides for which there's a versioned one in perl-*:
cat << \EOF > %{name}-perl-prov
#!/bin/sh
%{__perl_provides} $* \
| grep -v 'perl(APR::\(Request\(::\(Apache2\|CGI\|Error\)\)\?\))$' \
| grep -v 'perl(Apache2::\(Cookie\|Request\|Upload\))$'
EOF
%define __perl_provides %{_builddir}/%{name}-%{version}/%{name}-perl-prov
chmod +x %{__perl_provides}

# Fix up paths in doc tag files:
# ap*-1-config in FC5, ap*-config in earlier
%{__perl} -pi -e \
  "s|<path>.*?</path>|<path>%{_docdir}/%{name}-devel/</path>|" \
  docs/apreq2.tag
%{__perl} -pi -e \
  "s|<path>.*?</path>|<path>%{_docdir}/apr-devel/html/</path>|" \
  docs/apr.tag
%{__perl} -pi -e \
  "s|<path>.*?</path>|<path>%{_docdir}/apr-util-devel/html/</path>|" \
  docs/apu.tag

%patch -P 0
%patch -P 1
%patch -P 2
%patch -P 3 -p1
%patch -P 4 -p1

cp %{SOURCE2} .

./buildconf

%build
CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing" \
%configure \
  --disable-dependency-tracking \
  --disable-static \
  --with-apache2-apxs=%{_httpd_apxs} \
  --enable-perl-glue \
  --with-mm-opts=INSTALLDIRS=vendor
make %{?_smp_mflags}

# Fix multilib
sed -i -e 's,^libdir=.*,libdir="`pkg-config --variable=libdir %{name}`",' \
       -e 's,^LDFLAGS=.*,LDFLAGS="`pkg-config --libs %{name}`",' \
       -e 's,^LIBS=.*,LIBS="`pkg-config --libs %{name}`",' \
       -e 's,^INCLUDES=.*,INCLUDES="`pkg-config --cflags-only-I %{name}`",' \
        apreq2-config

%install
rm -rf $RPM_BUILD_ROOT __docs
mkdir -p $RPM_BUILD_ROOT%{_libdir}/pkgconfig

# Remove %optflags from the PC file
sed -i -e 's@%{optflags}@@' %{name}.pc
install -m 644 %{name}.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig
PKG_CONFIG_PATH=$RPM_BUILD_ROOT%{_libdir}/pkgconfig make install DESTDIR=$RPM_BUILD_ROOT

install -Dpm 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_httpd_modconfdir}/apreq.conf
cp -pR docs/html __docs
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
# make test # requires write access to system locations?

%ldconfig_scriptlets

%files
%doc CHANGES LICENSE NOTICE README
%config(noreplace) %{_httpd_modconfdir}/apreq.conf
%{_libdir}/httpd/modules/mod_apreq2.so

%files libs
%{_libdir}/libapreq2.so.*

%files devel
%doc STATUS __docs/* docs/*.tag
%{_bindir}/apreq2-config
%{_includedir}/apreq2/
%{_includedir}/httpd/apreq2/
%{_libdir}/libapreq2.so
%{_libdir}/pkgconfig/*.pc

%files -n perl-%{name}
%doc glue/perl/README
%{perl_vendorarch}/auto/APR/
%{perl_vendorarch}/APR/
%{perl_vendorarch}/Apache2/
%{_mandir}/man3/A*::*.3*

%changelog
%autochangelog
