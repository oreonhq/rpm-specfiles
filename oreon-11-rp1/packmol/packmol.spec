%global source0_hash b22451ae0963572dc2dbcdf15b7ee4cdd0f91a24402cb3deab00325375491583

Name:		packmol
Version:	21.1.0
Release:	3%{?dist}
Summary:	Packing optimization for molecular dynamics simulations
License:	MIT
URL:		https://m3g.github.io/packmol
Source0:	https://github.com/m3g/packmol/archive/v%{version}/packmol-%{version}.tar.gz
# Example files
Source2:        https://m3g.github.io/packmol/examples/examples.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc-gfortran

%description
Packmol creates an initial point for molecular dynamics simulations by
packing molecules in defined regions of space. The packing guarantees
that short range repulsive interactions do not disrupt the
simulations.

The great variety of types of spatial constraints that can be
attributed to the molecules, or atoms within the molecules, makes it
easy to create ordered systems, such as lamellar, spherical or tubular
lipid layers.

The user must provide only the coordinates of one molecule of each
type, the number of molecules of each type and the spatial constraints
that each type of molecule must satisfy.

The package is compatible with input files of PDB, TINKER, XYZ and
MOLDY formats.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
find . -name \*.o -delete
tar zxvf %{SOURCE2}

%build
# TODO: Please submit an issue to upstream (rhbz#2381351)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
export FC=gfortran
%cmake
%cmake_build

%install
%cmake_install
install -D -p -m 755 solvate.tcl %{buildroot}%{_bindir}/packmol_solvate

%check
cd examples
for f in interface.inp; do
    out=$(basename $f .inp).out
    ../redhat-linux-build/packmol < $f | tee  $out
    ok=$(grep "Success" $out|wc -l)
    if(( ! $ok )); then
	echo "Example failed to run"
	exit
    fi
done

%files
%doc AUTHORS
%license LICENSE
%{_bindir}/packmol
%{_bindir}/packmol_solvate

%changelog
%autochangelog
