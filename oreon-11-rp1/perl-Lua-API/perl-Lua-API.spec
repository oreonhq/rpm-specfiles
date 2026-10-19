%global source0_hash 5dd3652d221c8f3bd8df4c2af9898808a393e0b217b93129270db7319f4d161e
Name:           perl-Lua-API
Version:        0.04
Release:        1%{?dist}
Summary:        Interface to Lua's embedding API
License:        GPL-3.0-or-later
URL:            https://metacpan.org/release/Lua-API
Source0:        http://www.cpan.org/authors/id/D/DJ/DJERIUS/Lua-API-%{version}.tar.gz
Requires:       perl(XSLoader) >= 0.1
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Devel::PPPort)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::ParseXS)
BuildRequires:  perl(Test::Class)
BuildRequires:  perl(Test::Compile)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(lua-5.1)
# /oreon:deps
%description
Lua is a simple, expressive, extension programming language that is easily
embeddable. Lua::API provides Perl bindings to Lua's C-based embedding
API. It allows Perl routines to be called from Lua as if they were written
in C, and allows Perl routines to directly manipulate the Lua interpreter
and its environment. It presents a very low-level interface (essentially
equivalent to the C interface), so is aimed at developers who need that
sort of access.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Lua-API-%{version}
%oreon_prep
%build

export LUA_INC=$(pkg-config --cflags lua-5.1)
export LUA_LIBS=$(pkg-config --libs lua-5.1)
PERL_USE_UNSAFE_INC=1 %{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build
%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
chmod 0755 %{buildroot}%{perl_vendorarch}/auto/Lua/API/API.so
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
