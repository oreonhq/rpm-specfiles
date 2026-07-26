%global source0_hash bfb909037da678a1668f3f7f86efee7ee31f2bc66d90b83dd9e6b6a5f998c4e2

Name:           myrepos
Version:        1.20180726
Release:        23%{?dist}
Summary:        A multiple SCM repository management tool

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/joeyh/myrepos
Source0:        https://git.joeyh.name/index.cgi/myrepos.git/snapshot/myrepos-%{version}.tar.gz
Source1:        README.fedora
BuildArch:      noarch

Provides:       mr = %{version}-%{release}
Obsoletes:      mr < 1.15-6

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-podlators

Requires:       perl(File::Copy)
# Out off the box only git is supported. For additional details the 
# README.fedora lists the supported SCM tools. 
Requires:       git

%description
The mr command can checkout, update, or perform other actions on
a set of repositories as if they were one combined repository. It
supports any combination of subversion, git, cvs, mecurial, bzr and
darcs repositories, and support for other revision control systems
can easily be added.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
cp %{SOURCE1} .

%build
make %{?_smp_mflags}

%install
install -Dp -m 0755 mr %{buildroot}%{_bindir}/mr
for file in mr.1 webcheckout.1; do
    install -Dp -m 0644 $file %{buildroot}%{_mandir}/man1/$file
done
for file in lib/git-fake-bare lib/git-svn lib/unison; do
    install -Dp -m 0644 $file %{buildroot}%{_datadir}/mr/$file
done

%files
%doc README mrconfig mrconfig.complex README.fedora
%license GPL
%{_mandir}/man1/*.*
%{_bindir}/mr
%{_datadir}/mr/

%changelog
%autochangelog
