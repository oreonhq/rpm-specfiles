%global source0_hash 5895d332ec8d87e15f21441c61545b7f68830a2ee2c967d381773bd08504806d

Name:           mac-robber
Version:        1.02
Release:        32%{?dist}
Summary:        Tool to create a timeline of file activity for mounted file systems

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://sourceforge.net/projects/mac-robber/
Source0:        http://downloads.sourceforge.net/mac-robber/mac-robber-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
mac-robber is a digital forensics and incident response tool that can be used
with The Sleuth Kit to create a timeline of file activity for mounted 
file systems.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%make_build GCC_OPT="%{optflags}"

%install
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 mac-robber %{buildroot}%{_bindir}

%files
%doc CHANGES README
%license COPYING
%{_bindir}/mac-robber

%changelog
%autochangelog
