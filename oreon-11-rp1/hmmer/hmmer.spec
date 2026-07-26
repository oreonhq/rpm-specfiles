%global source0_hash none

Name:           hmmer
Version:        3.3.2
Release:        12%{?dist}
Summary:        Biosequence analysis using profile hidden Markov models

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            http://hmmer.org
Source0:        http://eddylab.org/software/hmmer/hmmer-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  make
# HMMER3 requires SSE or VMX vector instructions - Bug 2112825
# VMX only works for big endian in HMMER3
# author says more arch will be supported in HMMER4 (no ETA)
ExcludeArch:    aarch64 ppc64le s390x
Patch0:         hmmer-3.3.2-chris.patch

%description
HMMER is used for searching sequence databases for sequence homologs, and for
making sequence alignments. It implements methods using probabilistic models
called profile hidden Markov models (profile HMMs).

%package easel
Summary: Easel collection of small tools

%description easel

Collection of additional small tools ("miniapps") from the Easel library.

%package doc
Summary: Documentation for hmmer
BuildArch: noarch

%description doc
This package includes documentation files for the hmmer software package.

%prep
%setup -q
%patch -P0 -p1 -b .chris

%build
%configure
make %{?_smp_mflags}

%check
make check

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
(cd easel; make install DESTDIR=$RPM_BUILD_ROOT)

%files
%license LICENSE
%{_bindir}/hmm*
%{_bindir}/alimask
%{_bindir}/jackhmmer
%{_bindir}/makehmmerdb
%{_bindir}/nhmmer
%{_bindir}/nhmmscan
%{_bindir}/phmmer
%{_mandir}/man1/hmm*
%{_mandir}/man1/alimask*
%{_mandir}/man1/jackhmmer*
%{_mandir}/man1/makehmmerdb*
%{_mandir}/man1/nhmmer*
%{_mandir}/man1/nhmmscan*
%{_mandir}/man1/phmmer*

%files easel
%{_bindir}/easel
%{_bindir}/esl-*
%{_mandir}/man1/esl-*

%files doc
%doc LICENSE README.md RELEASE-%{version}.md Userguide.pdf tutorial/

%changelog
%autochangelog
