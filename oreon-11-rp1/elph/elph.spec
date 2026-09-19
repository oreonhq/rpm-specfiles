%global source0_hash 6d944401d2457d75815a34dbb5780f05df569eb1edfd00909b33c4c4c4ff40b9

Name:           elph
Version:        1.0.1
Release:        38%{?dist}
Summary:        Tool to find motifs in a set of DNA or protein sequences

# Automatically converted from old format: Artistic clarified - review is highly recommended.
License:        ClArtistic
URL:            http://www.cbcb.umd.edu/software/ELPH/
Source0:        ftp://ftp.cbcb.umd.edu/pub/software/elph/ELPH-1.0.1.tar.gz
Patch0:         %{name}-chris.patch
BuildRequires:  gcc-c++
BuildRequires: make

%description
ELPH is a general-purpose Gibbs sampler for finding motifs in a set of
DNA or protein sequences. The program takes as input a set containing
anywhere from a few dozen to thousands of sequences, and searches
through them for the most common motif, assuming that each sequence
contains one copy of the motif.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ELPH
%patch -P0 -p 1 -b .chris

%build
make -C sources %{?_smp_mflags} \
  CFLAGS="$RPM_OPT_FLAGS -fno-exceptions -fno-rtti -D_REENTRANT"

%check

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 sources/elph $RPM_BUILD_ROOT/%{_bindir}

%files
%doc COPYRIGHT LICENSE README Readme.ELPH VERSION
%{_bindir}/elph

%changelog
%autochangelog
