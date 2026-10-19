%global source0_hash 95138ce05786584d575a22583dd03df0e4b5339f459b2d9deabf3212e0736faa
Name:           git2cl
Version:        3.0
Release:        1%{?dist}
Summary:        Converts git logs to GNU style ChangeLog format
License:        GPL-2.0-or-later
URL:            https://savannah.nongnu.org/projects/git2cl
Source0:        https://git.savannah.gnu.org/cgit/git2cl.git/snapshot/git2cl-%{version}.tar.gz
BuildArch:      noarch
Requires:       git
# oreon:deps
BuildRequires:  perl-generators
# /oreon:deps
%description
A quick tool to convert git logs to GNU ChangeLog format.

The tool invokes git log internally unless you pipe a log to it. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir git2cl-%{version}
%oreon_prep
%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -p -m 755 git2cl $RPM_BUILD_ROOT%{_bindir}/git2cl
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
