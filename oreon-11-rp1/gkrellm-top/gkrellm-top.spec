%global source0_hash b2585c4186cc3805fcde73645a71d8eb3f798358caeb31cf3f598795e6ea42e6

%global gkplugindir %{_libdir}/gkrellm2/plugins

Summary:        GKrellM plugin which shows 3 most CPU intensive processes
Name:           gkrellm-top
Version:        2.2.13
Release:        31%{?dist}
License:        GPL-1.0-or-later
URL:            http://gkrelltop.sourceforge.net/
Source0:        https://downloads.sourceforge.net/gkrelltop/gkrelltop_%{version}.orig.tar.gz
Patch0:         gkrelltop-2.2.13-optflags.patch
Requires:       gkrellm >= 2.2.0
BuildRequires:  gcc
BuildRequires:  gkrellm-devel >= 2.2.0
BuildRequires:  make

%description
A GKrellM plugin which displays the top three CPU intensive processes in a
small window inside GKrellM, similar to wmtop. Useful to check out anytime
what processes are consuming most CPU power on your machine.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n gkrelltop-%{version}.orig
%patch -P0 -p1 -b .optflags

%build
%make_build

%install
install -D -m 755 gkrelltop.so $RPM_BUILD_ROOT%{gkplugindir}/gkrelltop.so
install -D -m 755 gkrelltopd.so $RPM_BUILD_ROOT%{gkplugindir}/gkrelltopd.so

%files
%doc README
%{gkplugindir}/gkrelltop.so
%{gkplugindir}/gkrelltopd.so

%changelog
%autochangelog
