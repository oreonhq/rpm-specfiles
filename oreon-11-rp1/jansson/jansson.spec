# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 c739578bf6b764aa0752db9a2fdadcfe921c78f1228c7ec0bb47fa804c55d17b
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

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
%oreon_verify_sources
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
