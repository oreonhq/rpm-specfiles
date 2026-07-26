%global source0_hash 2fa7776261d5cbfc969191ed11986e4ca7cb339a91e8b6435c9342828ea1626a

%global debug_package %{nil}

%global _description %{expand:
This library makes the SQLite3 API more friendly to C++ users. It supports
almost all of SQLite3 features using C++ classes such as database, command,
query, and transaction. The query class supports iterator concept for fetching
records. With ext::function class, it's also easy to use the sqlite3's
functions and aggregations in C++.}

Name:           sqlite3pp
Version:        1.0.9
Release:        %autorelease
Summary:        C++ wrapper of SQLite3 API

License:        MIT
URL:            https://github.com/iwongu/sqlite3pp
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  sqlite-devel

%description    %_description

%package        devel
Summary:        %{summary}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
Requires:       sqlite-devel

%description    devel %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
mkdir build
for f in test/*; do
  $CXX -I headeronly_src $CXXFLAGS -o "build/$(basename "$f" .cpp)" $f -lsqlite3 $LDFLAGS
done

%install
install -Dpm0644 -t %{buildroot}%{_includedir}/%{name} headeronly_src/*

%check
for f in build/*; do
  echo "Running $(basename "$f")"
  ./$f
done

%files devel
%license LICENSE
%doc README.md
%{_includedir}/%{name}/

%changelog
%autochangelog
