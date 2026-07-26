%global source0_hash 3bbccde25f942129450f34d6d4975f4234958072540e758bc131bb7960716d63

Name:           txt2regex
Version:        0.9
Release:        16%{?dist}
Summary:        Regular expression wizard that converts human sentences to regexes

License:        GPL-2.0-only
URL:            https://aurelio.net/projects/txt2regex/
Source0:        https://github.com/aureliojargas/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

# This removes the "TEXTDOMAINDIR=..." line from txt2regex. It isn't needed in
# Fedora where the default value is OK.
Patch0:         txt2regex-no-TEXTDOMAINDIR.patch

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  gettext
Requires:       bash >= 3.0

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
# nothing to do

%install

# install txt2regex and locale files
make DESTDIR=%{buildroot} install

# install man page
mkdir -p %{buildroot}/%{_mandir}/man1
install -p -m 644 man/txt2regex.man %{buildroot}%{_mandir}/man1/txt2regex.1

# find locale files
%find_lang %{name}

%files -f %{name}.lang
%doc CHANGELOG.md CONTRIBUTING.md README.md TODO
%license COPYRIGHT
%{_bindir}/txt2regex
%{_mandir}/man1/txt2regex.1*

%changelog
%autochangelog
