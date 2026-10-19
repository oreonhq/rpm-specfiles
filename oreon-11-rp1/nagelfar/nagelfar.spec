%global source0_hash 3baf920fb34b73e32067118365d074d859298e2bce3748ad9458624bece85b23
%global versionnodot 135
Name:           nagelfar
Version:        1.3.5
Release:        1%{?dist}
Summary:        Syntax checker for Tcl
License:        GPL-2.0-or-later
URL:            http://nagelfar.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}%{versionnodot}.tar.gz
Patch0:         use-datadir-to-store-aux-files.patch
Patch1:         tclsh-as-shebang.patch
Patch2:         script-to-test-install.patch
BuildArch:      noarch
Requires:       tcl
Requires:       tk
# oreon:deps
BuildRequires:  tcl
# /oreon:deps
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
ln -s syntaxdb86.tcl %{buildroot}%{_datadir}/%{name}/syntaxdb.tcl
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
%oreon_autofiles main

%check

./test_nagelfar.sh %{buildroot}%{_bindir}/nagelfar.tcl\
    %{buildroot}%{_datadir}/%{name}/syntaxdb.tcl\
    misctests/test.tcl
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
