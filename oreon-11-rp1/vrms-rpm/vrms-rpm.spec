%global source0_hash 91a737da17cc03a74770ccc8442631c2dd5e8ba40688de9f66c4f10605b418b6

Name:          vrms-rpm
Summary:       Report non-free software
License:       GPL-3.0-only

Version:       2.4
Release:       1%{?dist}

BuildRequires: gcc
BuildRequires: gettext-devel
BuildRequires: libcmocka-devel
BuildRequires: make
BuildRequires: rpm-devel
BuildRequires: python3-jsonschema

%global git_tag release-%{version}
URL:           https://github.com/suve/%{name}
Source0:       %{url}/archive/%{git_tag}/%{name}-%{git_tag}.tar.gz

%description
vrms-rpm ("virtual Richard M. Stallman") reports non-free packages
installed on the system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{git_tag}

%build
make all PREFIX=%{_prefix} %{?_smp_mflags} \
	DEFAULT_GRAMMAR=spdx-lenient \
	DEFAULT_LICENCE_LIST=fedora

%check
make test %{?_smp_mflags}
./build/vrms-rpm \
	--licence-list $(pwd)/build/licences/fedora.txt \
	--format json \
	| jsonschema ./docs/json-schema.json

%install
%make_install PREFIX=%{_prefix}
%find_lang %{name} --with-man

%files -f %{name}.lang
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%{_datadir}/suve/
%{_datadir}/bash-completion/completions/%{name}
%license LICENCE.txt IMAGE-CREDITS.txt

%changelog
%autochangelog
