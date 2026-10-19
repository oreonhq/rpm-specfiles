%global source0_hash 647bd88cd4836a186bf83b1d082db055307444a09a8fcd0decc619df277417bf
%global debug_package %{nil}
Name:           sqlite3pp
Version:        1.0.10
Release:        1%{?dist}
Summary:        C++ wrapper of SQLite3 API
License:        MIT
URL:            https://github.com/iwongu/sqlite3pp
Source0:        https://github.com/iwongu/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  sqlite-devel
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
Requires:       sqlite-devel
%description    devel

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

mkdir build
for f in test/*; do
  $CXX -I headeronly_src $CXXFLAGS -o "build/$(basename "$f" .cpp)" $f -lsqlite3 $LDFLAGS
done
%install
install -Dpm0644 -t %{buildroot}%{_includedir}/%{name} headeronly_src/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

for f in build/*; do
  echo "Running $(basename "$f")"
  ./$f
done
%files -f %{oreon_filedir}/main.list
%files -n sqlite3pp-devel -f %{oreon_filedir}/sqlite3pp-devel.list

%changelog

%autochangelog
