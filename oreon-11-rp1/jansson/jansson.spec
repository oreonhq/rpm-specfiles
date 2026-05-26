%global forgeurl https://github.com/akheron/jansson
Version:        2.14
%forgemeta

Name:		jansson
Release:	4%{?dist}
Summary:	C library for encoding, decoding and manipulating JSON data

# src/lookup3.h is LicenseRef-Fedora-Public-Domain
License:	MIT AND LicenseRef-Fedora-Public-Domain
URL:		%{forgeurl}
Source0:        https://github.com/akheron/jansson/archive/v2.14/jansson-2.14.tar.gz

# Fix the tests.
# Upstream commit 0677666f65b988b2dd44d02966a08fea490d5883
Patch:          0001-Fix-the-check-exports-tests-for-versioned-symbols.patch
# oreon url source checksums begin
%global source0_sha256 c739578bf6b764aa0752db9a2fdadcfe921c78f1228c7ec0bb47fa804c55d17b
%global source0_file jansson-2.14.tar.gz
# oreon url source checksums end

BuildRequires:	gcc
BuildRequires:	python3-sphinx
BuildRequires:  make
BuildRequires:  autoconf, automake, libtool

%description
Small library for parsing and writing JSON documents.

%package devel
Summary: Header files for jansson
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files for developing applications making use of jansson.

%package devel-doc
Summary: Development documentation for jansson
BuildArch: noarch

%description devel-doc
Development documentation for jansson.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/jansson-2.14.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "c739578bf6b764aa0752db9a2fdadcfe921c78f1228c7ec0bb47fa804c55d17b" || { echo "oreon: Source0 SHA256 mismatch for jansson-2.14.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%forgeautosetup -p1

%if 0%{?rhel} == 6
%{__sed} -i 's/code-block:: shell/code-block:: none/g' doc/*.rst
%endif

%build
autoreconf -f -i -v
%configure --disable-static
%make_build
make html

%check
make check

%install
%make_install
rm "$RPM_BUILD_ROOT%{_libdir}"/*.la

%files
%license LICENSE
%doc CHANGES
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/*

%files devel-doc
%doc doc/_build/html/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.14-4
- Prepare for Oreon 11 (RP1)
