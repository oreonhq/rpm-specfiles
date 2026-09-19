%global source0_hash 02ac62537ea34ee33b55efa41a832b78086548715298a454b6f304e29a7c9d43

Name: jsmn
Summary: Minimalistic JSON parser / tokenizer for C
License: MIT

%global git_date 20211014
%global git_commit 25647e692c7906b96ffd2b05ca54c097948e879c
%global git_sha %(c="%{git_commit}"; echo "${c:0:7}")

Version: 1.1.0^%{git_date}git%{git_sha}
Release: 4%{?dist}

URL: http://zserge.com/jsmn.html
Source0: https://github.com/zserge/jsmn/archive/%{git_commit}/jsmn-%{git_commit}.tar.gz

# Any debuginfo we generate along the way pertains only to tests.
%global debug_package %{nil}

BuildRequires: gcc
BuildRequires: make

# Main package is not "BuildArch: noarch"
# because we want to run the tests on all architectures.

%global desc %{expand:
jsmn (pronounced like 'jasmine') is a minimalistic JSON parser written in C.
It can be easily integrated into resource-limited or embedded projects.

Most JSON parsers offer you a bunch of functions to load JSON data, parse it
and extract any value by its name. jsmn proves that checking the correctness
of every JSON packet or allocating temporary objects to store parsed
JSON fields often is an overkill.

jsmn is designed to be robust (it should work fine even with erroneous data),
fast (it should parse data on the fly), portable (no superfluous dependencies
or non-standard C extensions). And of course, simplicity is a key feature:
simple code style, simple algorithm, simple integration into other projects.
}

%description %{desc}

%package devel
Summary: %{summary}
Provides: %{name}-static = %{version}-%{release}
BuildArch: noarch

%description devel %{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n jsmn-%{git_commit}

%build
# Nothing to do here

%install
install -m 755 -d %{buildroot}%{_includedir}/%{name}
install -m 644 -p jsmn.h %{buildroot}%{_includedir}/%{name}/%{name}.h

%check
%make_build test

%files devel
%doc README.md
%license LICENSE
%{_includedir}/%{name}

%changelog
%autochangelog
