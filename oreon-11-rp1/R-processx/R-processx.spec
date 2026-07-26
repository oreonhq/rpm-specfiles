%global source0_hash c5f1cafd0e4351caf512298888574a6b3bdd1b4d0fb42ef2834c7bf955734221

Name:           R-processx
Version:        %R_rpm_version 3.8.6
Release:        %autorelease
Summary:        Execute and Control System Processes

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Tools to run system processes in the background. It can check if a
background process is running; wait on a background process to finish; get
the exit status of finished processes; kill background processes. It can
read the standard output and error of the processes, using non-blocking
connections. 'processx' can poll a process for standard output or error,
with a timeout. It can also poll several processes at once.

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
%R_check \--no-tests

%files -f %{R_files}

%changelog
%autochangelog
