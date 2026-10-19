%global source0_hash e0ae93208666523344eada66713055cb7fd752bcdd2aa621b8a1783e22da3d17
Name:           aldo
Version:        0.7.7
Release:        1%{?dist}
Summary:        A morse tutor
License:        GPL-2.0-or-later AND GPL-3.0-or-later
URL:            http://aldo.nongnu.org/
Source0:        http://savannah.nongnu.org/download/aldo/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  libao-devel
BuildRequires:  make
# /oreon:deps
%description
Aldo is a morse code learning tool released under GPL, which provides
four type of training methods:

   1. Classic exercise : Identify random characters played in morse code.
   2. Koch method : Two morse characters will be played at full speed
      (20wpm) until you'll be able to identify at least 90 percent of
      them. After that, one more character will be added, and so on.
   3. Read from file : Identify the morse code generated from a file.
   4. Callsign exercise : Identify random callsigns played in morse code.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
