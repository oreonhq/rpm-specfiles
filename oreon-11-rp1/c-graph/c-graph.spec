%global source0_hash 2d267de3c9d75d8de95e5b51da11e7aa5e981291ee9a34ef6edcf8fea5084424

Name:		c-graph
Version:	2.0.1
Release:	17%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
Summary:	Convolution Graph
URL:		http://www.gnu.org/software/%{name}
Source0:	http://ftp.gnu.org/gnu/c-graph/%{name}-%{version}.tar.gz
BuildRequires:	gcc-gfortran
BuildRequires:	help2man
BuildRequires: make
Requires:	coreutils
Requires:	gnuplot
Requires:	ImageMagick
Requires:	less
Requires:	ncurses

%description
Convolution Theorem Visualization

Convolution is a core concept in today's cutting-edge technologies of
deep learning and computer vision. Singularly cogent in application to
digital signal processing, the convolution theorem is regarded as the
most powerful tool in modern scientific analysis. Long utilised for
accelerating the application of filters to images, fast training of
convolutional neural networks exploit the convolution theorem to accelerate
training and inference in the ubiquitous applications of computer vision
that, today, are at the vanguard of the evolving artificially intelligent
world in which we are becoming increasingly immersed.

Coded in modern Fortran, GNU C-Graph is the de facto tool for visualizing
convolution in university courses worldwide. "C-Graph" stands for
"Convolution Graph" - Free Software that makes learning about convolution
easy!

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
# remove \r\n line endings
sed -e 's|\r||' README > README.new
touch -r README.new README
mv README.new README
make %{?_smp_mflags} FCFLAGS="$FFLAGS"

%install
make install DESTDIR=%{buildroot}

# must be created when installing info
rm -f %{buildroot}%{_infodir}/dir

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%doc %{_docdir}/%{name}
%doc %{_infodir}/%{name}*
%doc %{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
