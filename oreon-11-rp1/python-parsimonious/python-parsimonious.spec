%global source0_hash 5fb1a5084d603e890d4fad10fd78ae10962a7a60810d18b2d723570dfd827055

Name:           python-parsimonious
Version:        0.10.0
Release:        %autorelease
Summary:        A fast pure-Python PEG parser

License:        MIT
URL:            https://github.com/erikrose/parsimonious
Source0:        %{url}/archive/%{version}/parsimonious-%{version}.tar.gz

BuildRequires:  python3-devel

BuildArch:      noarch

%description
Parsimonious aims to be the fastest arbitrary-lookahead parser written in pure
Python, and the most usable. It's based on parsing expression grammars (PEGs),
which means you feed it a simplified sort of EBNF notation. Parsimonious was
designed to undergird a MediaWiki parser that wouldn't take 5 seconds or a GB
of RAM to do one page, but it's applicable to all sorts of languages.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n parsimonious-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files parsimonious

%check
%tox

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
