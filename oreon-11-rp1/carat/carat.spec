%global source0_hash 31813f0b0579e003b56c80e6c95b58cbf1df8eaf9add65eab96ff528e548d8a9

# Get post-release bug fixes
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
Source0:        %{forgesource}
Source1:        %{name}.module.in
# Fix 2 use-after-free situations
# https://github.com/lbfm-rwth/carat/pull/107
Patch:          %{name}-use-after-free.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  environment(modules)
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  tex(latex)
BuildRequires:  tex(epic.sty)

Requires:       %{name}-tables = 1:%{version}-%{release}
Requires:       environment(modules)

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
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
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

# Build the documentation
cd tex
pdflatex manual
cd -

%install
# Install the binaries
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -dp bin/* %{buildroot}%{_libexecdir}/%{name}

# Install the environment-modules file
mkdir -p %{buildroot}%{_modulesdir}
sed 's#@LIBDIR@#'%{_libexecdir}/%{name}'#g;' < %{SOURCE1} \
  > %{buildroot}%{_modulesdir}/%{name}-%{_arch}
touch -r %{SOURCE1} %{buildroot}%{_modulesdir}/%{name}-%{_arch}

# Install the tables
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a tables %{buildroot}%{_datadir}/%{name}
rm %{buildroot}%{_datadir}/%{name}/tables/*.tar.gz
rm %{buildroot}%{_datadir}/%{name}/tables/lattices/{README.lattice,*.sh}
rm %{buildroot}%{_datadir}/%{name}/tables/qcatalog/*.sh
rm %{buildroot}%{_datadir}/%{name}/tables/symbol/{Makefile,README}

%check
cd tst
./run_all.sh
cd -

%files
%doc CHANGES.md README.md tex/README.short
%{_modulesdir}/%{name}-%{_arch}
%{_libexecdir}/%{name}/

%files tables
%doc tables/lattices/README.lattice
%license LICENSE
%{_datadir}/%{name}

%files doc
%doc tex/Graph tex/*.html tex/examples tex/manual.pdf tex/progs
%license LICENSE

%changelog
%autochangelog
