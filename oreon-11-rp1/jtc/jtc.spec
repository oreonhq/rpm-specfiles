%global source0_hash 61c561451c6dd75447f17a920137e604027759d4a82b533ecd9df2754a3df96f

%define tag_name LatestBuild
Name:           jtc
Version:        1.76a
Release:        14%{?dist}
Summary:        JSON processing utility

License:        MIT
URL:            https://github.com/ldn-softdev/jtc
Source0:        %{URL}/archive/%{tag_name}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++

%description
jtc stand for: JSON transformational chains (used to be JSON test console).

jtc offers a powerful way to select one or multiple elements from a source JSON
and apply various actions on the selected elements at once (wrap selected
elements into a new JSON, filter in/out, sort elements, update elements, insert
new elements, remove, copy, move, compare, transform, swap around and many other
operations).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{tag_name}

%build
g++ -std=gnu++14 %build_cxxflags -pthread -lpthread %{name}.cpp -o %{name}

%install
install -Dpm 0755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md
%doc "User Guide.md"
%doc "Walk-path tutorial.md"

%changelog
%autochangelog
