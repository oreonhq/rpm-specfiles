%global source0_hash 0fb85e21f5ffdd77198540fcb1e74182d7a86f088904164d6ba5c49385364d87
Name:           txt2regex
Version:        0.9
Release:        16%{?dist}
Summary:        Regular expression wizard that converts human sentences to regexes
License:        GPL-2.0-only
URL:            https://aurelio.net/projects/txt2regex/
Source0:        https://github.com/aureliojargas/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         txt2regex-no-TEXTDOMAINDIR.patch
BuildArch:      noarch
Requires:       bash >= 3.0
# oreon:deps
BuildRequires:  gettext
BuildRequires:  make
# /oreon:deps
%description
txt2regex is a regular expression wizard that converts human sentences to
regexes.

In a simple interactive interface, you just answer questions and build your
own regex for a large variety of software and programming languages.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

%build

%install
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}/%{_mandir}/man1
install -p -m 644 man/txt2regex.man %{buildroot}%{_mandir}/man1/txt2regex.1
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
