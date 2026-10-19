%global source0_hash 31813f0b0579e003b56c80e6c95b58cbf1df8eaf9add65eab96ff528e548d8a9
%global commit      fd0b757974c491203e050912c09ac0bd504c7700
%global date        20211018
%global forgeurl    https://github.com/lbfm-rwth/carat
Name:           carat
Epoch:          1
Version:        2.1
Summary:        Crystallographic AlgoRithms And Tables
%forgemeta
Release:        10%{?dist}
License:        GPL-2.0-or-later
URL:            https://lbfm-rwth.github.io/carat/
VCS:            git:%{forgeurl}.git
Source0:        %{forgeurl}/archive/%{commit}/%{name}-%{commit}.tar.gz
Source1:        %{name}.module.in
Patch:          %{name}-use-after-free.patch
ExcludeArch:    %{ix86}
Requires:       %{name}-tables = 1:%{version}-%{release}
Requires:       environment(modules)
# oreon:deps
BuildRequires:  environment(modules)
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  tex(epic.sty)
BuildRequires:  tex(latex)
# /oreon:deps
%description
CARAT handles enumeration, construction, recognition, and comparison problems
for crystallographic groups up to dimension 6.  The name CARAT is an acronym
for Crystallographic AlgoRithms And Tables.

Due to its specialized nature and some generically named binaries, this
package uses environment modules to access its binaries.

%package tables
Summary:        Tables for CARAT binaries
BuildArch:      noarch
%description tables
Tables for CARAT binaries to consume.

%package doc
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later
Summary:        Documentation and examples for CARAT
BuildArch:      noarch
%description doc
Documentation and examples for CARAT.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%conf
# Don't ship XV thumbnails with the examples
rm -fr tex/examples/.xvpics

# Generate configure
./autogen.sh

%build

%configure
%make_build
cd tex
pdflatex manual
cd -
%install
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -dp bin/* %{buildroot}%{_libexecdir}/%{name}
mkdir -p %{buildroot}%{_modulesdir}
sed 's#@LIBDIR@#'%{_libexecdir}/%{name}'#g;' < %{SOURCE1} \
  > %{buildroot}%{_modulesdir}/%{name}-%{_arch}
touch -r %{SOURCE1} %{buildroot}%{_modulesdir}/%{name}-%{_arch}
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a tables %{buildroot}%{_datadir}/%{name}
rm %{buildroot}%{_datadir}/%{name}/tables/*.tar.gz
rm %{buildroot}%{_datadir}/%{name}/tables/lattices/{README.lattice,*.sh}
rm %{buildroot}%{_datadir}/%{name}/tables/qcatalog/*.sh
rm %{buildroot}%{_datadir}/%{name}/tables/symbol/{Makefile,README}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

cd tst
./run_all.sh
cd -
%files -f %{oreon_filedir}/main.list
%files -n carat-tables -f %{oreon_filedir}/carat-tables.list
%files -n carat-doc -f %{oreon_filedir}/carat-doc.list

%changelog

%autochangelog
