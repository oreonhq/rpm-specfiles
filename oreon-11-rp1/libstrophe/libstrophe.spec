%global source0_hash d079668474d5c3aa4555347c33e77014a1071629603557cc506a6bc6f82e01f5

Name:           libstrophe
Version:        0.14.0
Release:        3%{?dist}
Summary:        An XMPP library for C

License:        MIT AND GPL-3.0-only
URL:            https://strophe.im/%{name}/
Source0:        https://github.com/strophe/libstrophe/releases/download/%{version}/libstrophe-%{version}.tar.gz
Source1:        https://github.com/strophe/libstrophe/releases/download/%{version}/libstrophe-%{version}.tar.gz.asc
# https://github.com/strophe/libstrophe/issues/253
Patch:          C23.patch
# https://keys.openpgp.org/search?q=F8ADC1F9A68A7AFF0E2C89E4391A5EFC2D1709DE
Source2:        F8ADC1F9A68A7AFF0E2C89E4391A5EFC2D1709DE.asc

BuildRequires:  gcc
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  zlib-devel
# expat or libxml, but no need for both
BuildRequires:  expat-devel
#BuildRequires:  libxml2-devel
BuildRequires:  openssl-devel
# For docs
BuildRequires:  doxygen
BuildRequires:  texinfo
# For signature verification
BuildRequires:  gpgverify

%description
libstrophe is a minimal XMPP library written in C. It has almost no
external dependencies, only an XML parsing library (expat or libxml
are both supported). It is designed for both POSIX and Windows
systems.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains docbook documentation for developing
applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i "s/GENERATE_DOCBOOK       = NO/GENERATE_DOCBOOK       = YES/g" Doxyfile
sed -i "s/GENERATE_HTML          = YES/GENERATE_HTML          = NO/g" Doxyfile

%build
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
autoreconf -i -W all
# expat is the default; use --with-libxml2 to switch
%configure --disable-static
%make_build
# Build docbook documentation
doxygen

%install
%make_install
# Removing libstrophe.la generated
rm -f %{buildroot}%{_libdir}/libstrophe.la

# Install examples/ dir shipping binary files generated
mkdir -p %{buildroot}%{_libdir}/%{name}/
cp -a examples/ %{buildroot}%{_libdir}/%{name}/
mv %{buildroot}%{_libdir}/%{name}/examples/.libs %{buildroot}%{_libdir}/%{name}/examples/libs
mv %{buildroot}%{_libdir}/%{name}/examples/.deps %{buildroot}%{_libdir}/%{name}/examples/deps
rm -f %{buildroot}%{_libdir}/%{name}/examples/.dirstamp
rm -f %{buildroot}%{_libdir}/%{name}/examples/deps/.dirstamp

# Install docbook documentation for the doc subpackage
mkdir -p %{buildroot}%{_datadir}/help/en/libstrophe
for file in docs/docbook/*.xml
do
  install -m644 ${file} %{buildroot}%{_datadir}/help/en/libstrophe/
done

%check
make check

%files
%license LICENSE.txt
%license GPL-LICENSE.txt
%license MIT-LICENSE.txt
%doc README
%doc AUTHORS
%doc ChangeLog 
%{_libdir}/%{name}.so.0*

%files devel
%doc examples/README.md
%{_includedir}/strophe.h
%{_libdir}/%{name}.so
%{_libdir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%license LICENSE.txt
%license GPL-LICENSE.txt
%license MIT-LICENSE.txt
%dir %{_datadir}/help/en
%lang(en) %{_datadir}/help/en/libstrophe

%changelog
%autochangelog
