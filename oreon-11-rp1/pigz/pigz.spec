%global source0_hash eb872b4f0e1f0ebe59c9f7bd8c506c4204893ba6a8492de31df416f0d5170fd0
Name:           pigz
Version:        2.8
Release:        1%{?dist}
Summary:        Parallel implementation of gzip
License:        Zlib
URL:            https://www.zlib.net/pigz/
Source0:        https://www.zlib.net/%{name}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncompress
BuildRequires:  zlib-devel
# /oreon:deps
%description
pigz, which stands for parallel implementation of gzip,
is a fully functional replacement for gzip that exploits
multiple processors and multiple cores to the hilt when
compressing data.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build CFLAGS="$RPM_OPT_FLAGS"
%install
install -p -D pigz $RPM_BUILD_ROOT%{_bindir}/pigz
pushd $RPM_BUILD_ROOT%{_bindir}; ln pigz unpigz; popd
install -p -D pigz.1 -m 0644 $RPM_BUILD_ROOT%{_datadir}/man/man1/pigz.1
%oreon_autofiles main

%check

make tests CFLAGS="$RPM_OPT_FLAGS"
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.8-1
- Prepare for Oreon 11 (RP1)
