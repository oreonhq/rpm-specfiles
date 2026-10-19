%global source0_hash 71b8d6e8f5fe81f6c6d0d110e3892251f6ce76ed095abd315e26e6e1193af3af
%bcond check 1
Name:           jq
Version:        1.8.2
Release:        1%{?dist}
Summary:        Command-line JSON processor
License:        MIT AND ICU AND CC-BY-3.0
URL:            https://jqlang.org/
Source0:        https://github.com/jqlang/jq/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
%ifarch %{valgrind_arches}
%endif
# oreon:deps
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  oniguruma-devel
BuildRequires:  tzdata
# /oreon:deps
%description
lightweight and flexible command-line JSON processor

 jq is like sed for JSON data – you can use it to slice
 and filter and map and transform structured data with
 the same ease that sed, awk, grep and friends let you
 play with text.

 It is written in portable C, and it has zero runtime
 dependencies.

 jq can mangle the data format that you have into the
 one that you want with very little effort, and the
 program to do so is often shorter and simpler than
 you'd expect.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CFLAGS="%{optflags} -ffp-contract=off \
-fno-builtin-exp -fno-builtin-log -fno-builtin-pow -fno-builtin-log2 -fno-builtin-exp2 \
-fno-builtin-sin -fno-builtin-cos -fno-builtin-sqrt -fno-builtin-ceil -fno-builtin-floor \
-fno-builtin-fmin -fno-builtin-fmax -fno-builtin-round -fno-builtin-trunc"
%configure --disable-static
%make_build
%install
%make_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%ifarch x86_64
make check
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n jq-devel -f %{oreon_filedir}/jq-devel.list

%changelog

%autochangelog
