%global source0_hash 95c051546b92f78bad374f8f99b5fd8e7390c488d2db07f34b3c1ee103c300ab
Name:           vinci
Version:        1.0.5
Release:        30%{?dist}
Summary:        Algorithms for volume computation
License:        GPL-1.0-or-later
URL:            https://www.multiprecision.org/vinci/
Source0:        https://www.multiprecision.org/downloads/%{name}-%{version}.tar.gz
Source1:        %{name}.1
ExcludeArch:    %{ix86}
Requires:       coreutils
Requires:       lrslib-utils
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  tex(latex)
# /oreon:deps
%description
The volume is one of the central properties of a convex body, and volume
computation is involved in many hard problems.  Applications range from rather
classical ones as in convex optimization to problems in remote fields like
algebraic geometry where the number of common roots of polynomials can be
related to a special polytope volume.

Part of the fascination of the subject stems from the discrepancy between the
intuitive notion of "volume" and the actual hardness of computing it.  Despite
this discouraging complexity — algorithms in general need exponential time in
the input dimension — steadily growing computer power enables us to attack
problems of practical interest.

Vinci is an easy to install C package that implements the state of the art
algorithms for volume computation.  It is the fruit of a research project
carried out at the IFOR (Institute for Operations Research) at ETH Zürich, in
collaboration with Benno Büeler and Komei Fukuda.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

sed -i 's|-o vinci|& %{build_ldflags}|' makefile
%make_build OPT='%{build_cflags}'
pdflatex manual.tex
pdflatex manual.tex
%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 %{name} %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
sed -e "s/@VERSION@/%{version}/" %{SOURCE1} > \
  %{buildroot}%{_mandir}/man1/%{name}.1
touch -r %{SOURCE1} %{buildroot}%{_mandir}/man1/%{name}.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
