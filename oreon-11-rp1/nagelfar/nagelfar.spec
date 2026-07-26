%global source0_hash 3baf920fb34b73e32067118365d074d859298e2bce3748ad9458624bece85b23

%global versionnodot 135

Name:           nagelfar
Version:        1.3.5
Release:        3%{?dist}
Summary:        Syntax checker for Tcl

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://nagelfar.sourceforge.net/
Source0:        http://downloads.sourceforge.net/nagelfar/%{name}%{versionnodot}.tar.gz

# Get auxiliary files from software-specific datadir
Patch0:         use-datadir-to-store-aux-files.patch
# Set tclsh as shebang for nagelfar.tcl script
Patch1:         tclsh-as-shebang.patch
# Add script to test Nagelfar installation
Patch2:         script-to-test-install.patch

BuildArch:      noarch

# tclsh needed for check step
BuildRequires:  tcl

Requires:       tcl
Requires:       tk

%description
Nagelfar is a Tcl application to read a Tcl program and provide static syntax
analysis - information regarding Tcl syntax errors like missing braces,
incomplete commands, etc. It is, moreover, extensible, with a customizable
exposed syntax database and plugins. Nagelfar has also support for doing
simple code coverage analysis.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}%{versionnodot}
%patch -P0
%patch -P1
%patch -P2
chmod +x test_nagelfar.sh

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{name}/
mv nagelfar.syntax %{buildroot}%{_datadir}/%{name}/
mv packagedb %{buildroot}%{_datadir}/%{name}/
mv syntaxbuild.tcl %{buildroot}%{_datadir}/%{name}/
mv syntaxdb86.tcl %{buildroot}%{_datadir}/%{name}/
mv syntaxdb87.tcl %{buildroot}%{_datadir}/%{name}/
mv syntaxdb90.tcl %{buildroot}%{_datadir}/%{name}/
# default syntaxdb points to Tcl 9.0 version on Fedora>=42, Tcl 8.6 elsewhere
%if 0%{?fedora} >= 42
ln -s syntaxdb90.tcl %{buildroot}%{_datadir}/%{name}/syntaxdb.tcl
%else
ln -s syntaxdb86.tcl %{buildroot}%{_datadir}/%{name}/syntaxdb.tcl
%endif

mkdir -p %{buildroot}%{_bindir}
mv nagelfar.tcl %{buildroot}%{_bindir}/

mv {doc/,}call-by-name.txt
mv {doc/,}codecoverage.txt
mv {doc/,}inlinecomments.txt
mv {doc/,}messages.txt
mv {doc/,}oo.txt
mv {doc/,}plugins.txt
mv {doc/,}README.txt
mv {doc/,}syntaxdatabases.txt
mv {doc/,}syntaxtokens.txt

%check
./test_nagelfar.sh %{buildroot}%{_bindir}/nagelfar.tcl\
    %{buildroot}%{_datadir}/%{name}/syntaxdb.tcl\
    misctests/test.tcl

%files
%license COPYING
%doc call-by-name.txt codecoverage.txt inlinecomments.txt messages.txt oo.txt plugins.txt README.txt syntaxdatabases.txt syntaxtokens.txt
%{_bindir}/nagelfar.tcl
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/nagelfar.syntax
%{_datadir}/%{name}/syntaxbuild.tcl
%{_datadir}/%{name}/syntaxdb86.tcl
%{_datadir}/%{name}/syntaxdb87.tcl
%{_datadir}/%{name}/syntaxdb90.tcl
%{_datadir}/%{name}/syntaxdb.tcl
%dir %{_datadir}/%{name}/packagedb
%{_datadir}/%{name}/packagedb/*

%changelog
%autochangelog
