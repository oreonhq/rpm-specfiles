%global source0_hash b81ffa8310da56565c77626b5a499f263c26f40ea857b233586d5fef391dd25e

Name:           R-sfsmisc
Version:        %R_rpm_version 1.1-23
Release:        %autorelease
Summary:        Utilities from 'Seminar fuer Statistik' ETH Zurich

License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel
BuildRequires:  procps-ng
Suggests:       procps-ng

%description
Useful utilities ['goodies'] from Seminar fuer Statistik ETH Zurich, some
of which were ported from S-plus in the 1990s. For graphics, have pretty
(Log-scale) axes, an enhanced Tukey-Anscombe plot, combining histogram and
boxplot, 2d-residual plots, a 'tachoPlot()', pretty arrows, etc. For
robustness, have a robust F test and robust range(). For system support,
notably on Linux, provides 'Sys.*()' functions with more access to system
and CPU information. Finally, miscellaneous utilities such as simple
efficient prime numbers, integer codes, Duplicated(), toLatex.numeric() and
is.whole().

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
