%global source0_hash 1df2463f94ebd926f402e7bcd92bf4a16f7a35732080a607fe4716888f1edbb5
%global debug_package %{nil}
%global commit b1ef26a55cdb60d236a5cb199c4234c704f46726
%global date   20210314
%global forgeurl https://github.com/orlp/pdqsort
Name:           pdqsort
Version:        0
Summary:        Pattern-defeating quicksort library
%forgemeta
Release:        1%{?dist}
License:        Zlib
URL:            %{forgeurl}
VCS:            git:%{forgeurl}.git
Source0:        %{forgeurl}/archive/%{commit}/%{name}-%{commit}.tar.gz
ExcludeArch:    %{ix86}
%global _desc %{expand:Pattern-defeating quicksort (pdqsort) is a novel sorting algorithm that
combines the fast average case of randomized quicksort with the fast worst
case of heapsort, while achieving linear time on inputs with certain patterns.
pdqsort is an extension and improvement of David Musser's introsort.}
# oreon:deps
BuildRequires:  gcc-c++
# /oreon:deps
%description
%_desc

%package        devel
Summary:        Pattern-defeating quicksort library
BuildArch:      noarch
Provides:       %{name}-static = %{version}-%{release}
%description    devel
%_desc

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup

%build

%install
mkdir -p %{buildroot}%{_includedir}
cp -p pdqsort.h %{buildroot}%{_includedir}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ifarch %{x86_64}
cd bench
sed -i 's/1000000, //' bench.cpp
g++ %{build_cxxflags} -o bench bench.cpp
./bench
cd -
%endif
%files -f %{oreon_filedir}/main.list
%files -n pdqsort-devel -f %{oreon_filedir}/pdqsort-devel.list

%changelog

%autochangelog
