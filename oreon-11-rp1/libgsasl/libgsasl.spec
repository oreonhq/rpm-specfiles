%global source0_hash f1b553384dedbd87478449775546a358d6f5140c15cccc8fb574136fdc77329f

Name:           libgsasl
Version:        1.10.0
Release:        14%{?dist}
Summary:        GNU SASL library
License:        LGPL-2.1-or-later
URL:            https://www.gnu.org/software/gsasl/
Source0:        https://ftp.gnu.org/gnu/gsasl/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/gsasl/%{name}-%{version}.tar.gz.sig
Source2:        https://josefsson.org/54265e8c.txt
BuildRequires:  gcc
# for %%gpgverify
BuildRequires:  gnupg2
BuildRequires:  krb5-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libidn-devel
BuildRequires:  libntlm-devel
BuildRequires:  make
BuildRequires:  pkgconfig

%description
The library includes support for the SASL framework
and at least partial support for the CRAM-MD5, EXTERNAL,
GSSAPI, ANONYMOUS, PLAIN, SECURID, DIGEST-MD5, LOGIN,
and NTLM mechanisms.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%configure --disable-static --disable-rpath --with-gssapi-impl=mit
%{make_build}

%install
%{make_install}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%doc AUTHORS NEWS README THANKS
%license COPYING COPYING.LIB
%{_libdir}/libgsasl.so.*

%files devel
%license COPYING COPYING.LIB
%{_includedir}/gsasl*
%{_libdir}/libgsasl.so
%{_libdir}/pkgconfig/libgsasl.pc

%changelog
%autochangelog
