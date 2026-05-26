# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 0ac299ad359e3f512b06a99397d025cfff81d3be34464ded0656f8a96676c029
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Summary: Tool for generating C, C++, and go recognizers from regular expressions
Name: re2c
Version: 3.1
Release: 6%{?dist}
License: LicenseRef-Public-Domain
URL: https://re2c.org/
Source: https://github.com/skvadrik/re2c/releases/download/%{version}/re2c-%{version}.tar.xz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: python3

%description
re2c is a tool for writing very fast and very flexible scanners. Unlike any
other such tool, re2c focuses on generating high efficient code for regular
expression matching. As a result this allows a much broader range of use than
any traditional lexer offers. And Last but not least re2c generates warning
free code that is equal to hand-written code in terms of size, speed and
quality.


%prep
%oreon_verify_sources
%setup -q


%build
%configure --disable-silent-rules
%make_build


%install
%make_install


%check
make tests


%files
%license LICENSE
%doc CHANGELOG README.md examples/ doc/*
%{_bindir}/re2c
%{_bindir}/re2go
%{_bindir}/re2rust
%{_datadir}/re2c/
%{_mandir}/man1/re2c.1*
%{_mandir}/man1/re2go.1*
%{_mandir}/man1/re2rust.1*


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.1-6
- Import
