%global source1_hash cee8cb413dc6e7c8ff8d2b1e88196b82e1d11158673638f1dfff67a6fcd58e74
%global source0_hash d1162965c61de44f72162fd87ec1394bd4f90f87bc8152d13fe4ae692fdc73fa
%global source2_key_fpr AC5D65F10C8596D7E2DAE2633D309B604AE3942E
%global _hardened_build 1
Name:           libvoikko
Version:        4.3.3
Release:        1%{?dist}
Summary:        Voikko is a library for spellcheckers and hyphenators
License:        GPL-2.0-or-later
URL:            https://voikko.puimula.org
Source0:        https://www.puimula.org/voikko-sources/%{name}/%{name}-%{version}.tar.gz
Source1:        http://www.puimula.org/voikko-sources/%{name}/%{name}-%{version}.tar.gz.asc
Source2:        gpgkey-AC5D65F10C8596D7E2DAE2633D309B604AE3942E.gpg
Requires: voikko-fi
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  python3-devel
# /oreon:deps
%description
This is libvoikko, library for spellcheckers and hyphenators using Malaga
natural language grammar development tool. The library is written in C.

Currently only Finnish is supported, but the API of the library has been
designed to allow adding support for other languages later. Note however that
Malaga is rather low level tool that requires implementing the whole morphology
of a language as a left associative grammar. Therefore languages that have
simple or even moderately complex morphologies and do not require morphological
analysis in their hyphenators should be implemented using other tools such as
Hunspell.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n     voikko-tools
Summary:        Test tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n voikko-tools
This package contains voikkospell and voikkohyphenate, small command line
tools for testing libvoikko. These tools may also be useful for shell
scripts.

%package -n python3-libvoikko
Summary:        Python interface to %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description -n python3-libvoikko
Python interface to libvoikko, library of Finnish language tools.
This module can be used to perform various natural language analysis
tasks on Finnish text.

%prep

%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%autosetup

%build

%configure --disable-hfst --with-dictionary-path=%{_prefix}/lib/voikko
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build CXXFLAGS="$CXXFLAGS"
%install
make install INSTALL="install -p" DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'
install -d $RPM_BUILD_ROOT%{python3_sitelib}
install -pm 0644 python/libvoikko.py $RPM_BUILD_ROOT%{python3_sitelib}/
mkdir -p %{buildroot}%{_prefix}/lib/voikko
%oreon_autofiles voikko-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-libvoikko usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n libvoikko-devel -f %{oreon_filedir}/libvoikko-devel.list
%files -n voikko-tools -f %{oreon_filedir}/voikko-tools.list
%files -n python3-libvoikko -f %{oreon_filedir}/python3-libvoikko.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.3.3-1
- Prepare for Oreon 11 (RP1)
