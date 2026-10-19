%global source0_hash 4137a4b5d5d4d02b59f676e25c0c68bdabf109e1837eb48d6f1634b054ebafd0
Summary:        A set of commands for manipulating flat-text databases from the shell
Name: perl-Fsdb
Version: 3.17
Epoch: 2
Release:        1%{?dist}
License: GPL-2.0-only
URL: http://www.isi.edu/~johnh/SOFTWARE/FSDB/
Source0:        http://www.isi.edu/~johnh/SOFTWARE/FSDB/Fsdb-%{version}.tar.gz
BuildArch: noarch
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(HTML::Parser)
Requires:       perl(Text::CSV_XS)
Requires:       perl(IO::Compress::Bzip2)
Requires:       perl(IO::Compress::Gzip)
Requires:       perl(IO::Compress::Xz)
Requires:  perl(IPC::Cmd)
Requires:  perl(XML::Simple)
Requires:  perl(YAML::XS)
# oreon:deps
BuildRequires:  groff-base
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(IO::Compress::Bzip2)
BuildRequires:  perl(IO::Compress::Gzip)
BuildRequires:  perl(IO::Compress::Xz)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Uncompress::AnyUncompress)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Pod::Html)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::CSV_XS)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(YAML::XS)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-podlators
# /oreon:deps
%description
FSDB is a package of commands for manipulating flat-ASCII databases from
shell scripts.  FSDB is useful to process medium amounts of data (with
very little data you'd do it by hand, with megabytes you might want a
real database).  FSDB is very good at doing things like:

        - extracting measurements from experimental output
        - re-examining data to address different hypotheses
        - joining data from different experiments
        - eliminating/detecting outliers
        - computing statistics on data (mean, confidence intervals,
                correlations, histograms)
        - reformatting data for graphing programs

Rather than hand-code scripts to do each special case, FSDB provides
higher-level functions than one gets with raw perl or shell scripts.
(Some features:  control uses names instead of column numbers,
it is self-documenting, and is robust with good error and memory handling.)

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Fsdb-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -exec chmod g-s {} ';'
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
