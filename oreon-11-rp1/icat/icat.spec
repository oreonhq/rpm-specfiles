%global source0_hash 5fcd9e6a1fe0b68ff1b3025cf0a3f09dfadf7471876783b5e49394a669e5efe1

%global repo_owner atextor
%global repo_name  icat

Name:    icat
Summary: Output images in terminal
License: BSD-2-Clause

%global git_commit 9b5aa622fdfbfbd37a97c9b8d3258100e1d26cd6
%global git_date   20230110
%global git_short  %(c="%{git_commit}"; echo "${c:0:7}")

Version: 0.5
Release: 22.%{git_date}git%{git_short}%{?dist}

URL:     https://github.com/%{repo_owner}/%{repo_name}
Source0: %{URL}/archive/%{git_commit}/%{repo_name}-%{git_commit}.tar.gz

BuildRequires: gcc
BuildRequires: imlib2-devel
BuildRequires: make

# sleuthkit provides a completely unrelated /usr/bin/icat
Conflicts: sleuthkit

%description
Outputs an image on a 256-color or 24-bit color enabled terminal
with UTF-8 locale, such as gnome-terminal, konsole or rxvt-unicode (urxvt).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{repo_name}-%{git_commit}
# Extract license from source code
awk '1;/\*\//{exit}' < icat.c > LICENSE

%build
%make_build

%install
install -m 755 -d %{buildroot}/%{_bindir}
install -m 755 ./icat %{buildroot}/%{_bindir}/icat

install -m 755 -d %{buildroot}/%{_mandir}/man1
install -m 644 ./icat.man %{buildroot}/%{_mandir}/man1/%{name}.1

%files
%doc CHANGELOG README.md
%license LICENSE
%{_bindir}/icat
%{_mandir}/man1/*

%changelog
%autochangelog
