%global source0_hash 3944efdabb685748482bfd6d7e7aaa392cfd686dedb38fbf59277b1fa3a48a65

Summary: A simple program for calculating radial velocities of stars in a binary system
Name: radial
Version: 1.0
Release: 35%{?dist}
License: LicenseRef-Fedora-UltraPermissive
Url: http://www.nhn.ou.edu/~hegarty/radial/
Source0: http://www.nhn.ou.edu/~hegarty/radial/%{name}-%{version}.tar.gz
Source1: http://www.nhn.ou.edu/~hegarty/radial/%{name}-%{version}.f

BuildRequires: gcc-gfortran

%description
This program calculates the radial velocities of
both stars in a binary system, allowing for user
configuration of stellar masses, semimajor axis,
inclination of orbital plane, orbital eccentricity,
time to collect data, and calculation frequency.

For your convenience, default values have been
added to the program, so you can run it with
nothing other than variable eccentricity, if you like.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
cp -a %{SOURCE1} .

%build
gfortran %{optflags} -ffixed-line-length-none -o radial %{name}-%{version}.f

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%doc README INSTALL
%{_bindir}/radial

%changelog
%autochangelog
