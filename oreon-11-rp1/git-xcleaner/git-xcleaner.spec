%global source0_hash e9a7ad466fb6eb453983cafd73289d1b0e0c62ddc305b05df3a479441c3fbbbc

Name:           git-xcleaner
Version:        3.1
Release:        3%{?dist}

Summary:        Interactive git branch removal TUI

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://github.com/lzap/git-xcleaner
Source:         https://github.com/lzap/git-xcleaner/archive/refs/tags/%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  sed
BuildRequires:  rubygem-ronn
Requires:       /usr/bin/resize
Requires:       newt

%description
git-xcleaner helps with deleting unused topic branches using TUI (text user
interface). It also offers mechanisms for pre-selecting branches that can be
safely removed.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%build
# Man page and ANSII-only text version of the man page for the embedded help
ronn man/%{name}.md
ronn -m man/%{name}.md | sed -r 's/\x1b\[[0-9;]*m?//g' > man/%{name}.1.txt

%install
rm -rf $RPM_BUILD_ROOT

install -Dp %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dpm 644 man/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%files
%doc LICENSE README.md man/%{name}.1.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
