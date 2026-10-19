%global source0_hash 3ba160ee5da720337c648f12dd7e4f384359cfc76b47f6a700689bdad08f6e43
Name:           git-xcleaner
Version:        4.0
Release:        1%{?dist}
Summary:        Interactive git branch removal TUI
License:        GPL-2.0-only
URL:            https://github.com/lzap/git-xcleaner
Source0:        https://github.com/lzap/git-xcleaner/archive/refs/tags/%{version}.tar.gz
BuildArch:      noarch
Requires:       /usr/bin/resize
Requires:       newt
# oreon:deps
BuildRequires:  rubygem-ronn
BuildRequires:  sed
# /oreon:deps
%description
git-xcleaner helps with deleting unused topic branches using TUI (text user
interface). It also offers mechanisms for pre-selecting branches that can be
safely removed.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%build

ronn man/%{name}.md
ronn -m man/%{name}.md | sed -r 's/\x1b\[[0-9;]*m?//g' > man/%{name}.1.txt
%install
rm -rf $RPM_BUILD_ROOT
install -Dp %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dpm 644 man/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
