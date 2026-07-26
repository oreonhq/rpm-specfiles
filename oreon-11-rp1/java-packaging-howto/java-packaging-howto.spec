%global source0_hash 24f1dca4bdc093647d5c746e1ed28e411e397d7d99b14868194e068a06decb85

Name:           java-packaging-howto
Version:        40.0.1
Release:        7%{?dist}
Summary:        Fedora Java packaging HowTo
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/fedora-java/howto
BuildArch:      noarch

Source0:        https://github.com/fedora-java/howto/archive/%{version}.tar.gz

BuildRequires:  make
BuildRequires:  asciidoctor
BuildRequires:  dia
BuildRequires:  man
BuildRequires:  colorized-logs
BuildRequires:  maven-local-openjdk25

%description
Offline version of Fedora Java packaging HowTo.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n howto-%{version}

%build
make clean-all all

%install
# nothing to install

%files
%license LICENSE
%doc index.html

%changelog
%autochangelog
