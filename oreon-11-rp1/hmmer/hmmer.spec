%global source0_hash ca70d94fd0cf271bd7063423aabb116d42de533117343a9b27a65c17ff06fbf3
Name:           hmmer
Version:        3.4
Release:        1%{?dist}
Summary:        Biosequence analysis using profile hidden Markov models
License:        GPL-3.0-only
URL:            http://hmmer.org
Source0:        http://eddylab.org/software/hmmer/hmmer-%{version}.tar.gz
ExcludeArch:    aarch64 ppc64le s390x
Patch0:         hmmer-3.3.2-chris.patch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n hmmer-easel -f %{oreon_filedir}/hmmer-easel.list
%files -n hmmer-doc -f %{oreon_filedir}/hmmer-doc.list

%changelog

%autochangelog
