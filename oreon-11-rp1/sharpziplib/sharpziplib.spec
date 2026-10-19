%global source0_hash 92678f2b5e4ec2ca6df598ef6d3bbf57f0176ada2e4901f689d844f7744fe9c6
%global libname SharpZipLib
%global debug_package %{nil}
%bcond_with brokentests
Name:           sharpziplib
Version:        1.4.2
Release:        1%{?dist}
Summary:        Zip, GZip, Tar and BZip2 library
License:        LicenseRef-Callaway-GPLv2+-with-exceptions AND LicenseRef-Callaway-BSD AND Zlib
URL:            http://icsharpcode.github.io/%{libname}
Source0:        https://github.com/icsharpcode/%{name}/archive/v%{version}.tar.gz#/%{libname}-%{version}.tar.gz
ExclusiveArch:  %{mono_arches}
Requires:       mono-core
# oreon:deps
BuildRequires:  mono-devel
# /oreon:deps
%description
SharpZipLib, formerly NZipLib is a Zip, GZip, Tar and BZip2 library
written entirely in C# . It is implemented as an assembly (installable
in the GAC), and thus can easily be incorporated into other projects.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn%{libname}-%{version}

%build

mkdir bin
cd src/ICSharpCode.SharpZipLib/
cat > AssemblyInfo.cs << FINISH
using System.Reflection;
// General Information about an assembly is controlled through the following 
// set of attributes. Change these attribute values to modify the information
// associated with an assembly.
[assembly: AssemblyTitle("SharpZipLib")]
[assembly: AssemblyVersion("%{version}")]
[assembly: AssemblyDescription("C# Zip, GZip, Tar and BZip2 library for .NET")]
[assembly: AssemblyCulture("")]
FINISH
mcs ./Lzw/LzwException.cs ./Lzw/LzwInputStream.cs ./Lzw/LzwConstants.cs ./Core/Exceptions/StreamDecodingException.cs \
    ./Core/Exceptions/SharpZipBaseException.cs ./Core/Exceptions/ValueOutOfRangeException.cs \
    ./Core/Exceptions/StreamUnsupportedException.cs ./Core/Exceptions/UnexpectedEndOfStreamException.cs \
    ./Core/EmptyRefs.cs \
    ./Core/InvalidNameException.cs ./Core/FileSystemScanner.cs ./Core/INameTransform.cs ./Core/PathFilter.cs \
    ./Core/PathUtils.cs ./Core/StreamUtils.cs ./Core/IScanFilter.cs ./Core/NameFilter.cs \
    ./BZip2/BZip2.cs ./BZip2/BZip2Exception.cs ./BZip2/BZip2InputStream.cs ./BZip2/BZip2OutputStream.cs ./BZip2/BZip2Constants.cs \
    ./Zip/ZipHelperStream.cs ./Zip/FastZip.cs ./Zip/IEntryFactory.cs ./Zip/Compression/InflaterHuffmanTree.cs \
    ./Zip/Compression/InflaterDynHeader.cs ./Zip/Compression/Deflater.cs ./Zip/Compression/DeflaterEngine.cs \
    ./Zip/Compression/DeflaterHuffman.cs ./Zip/Compression/DeflaterConstants.cs ./Zip/Compression/PendingBuffer.cs \
    ./Zip/Compression/Streams/InflaterInputStream.cs ./Zip/Compression/Streams/StreamManipulator.cs \
    ./Zip/Compression/Streams/DeflaterOutputStream.cs ./Zip/Compression/Streams/OutputWindow.cs ./Zip/Compression/Inflater.cs \
    ./Zip/Compression/DeflaterPending.cs ./Zip/ZipException.cs ./Zip/ZipEntryFactory.cs ./Zip/ZipFile.cs ./Zip/ZipExtraData.cs \
    ./Zip/ZipEntryExtensions.cs \
    ./Zip/ZipEntry.cs ./Zip/ZipNameTransform.cs ./Zip/ZipInputStream.cs ./Zip/ZipOutputStream.cs ./Zip/ZipConstants.cs \
    ./Zip/ZipStrings.cs ./Zip/WindowsNameTransform.cs \
    ./Zip/ZipEncryptionMethod.cs \
    ./Tar/TarInputStream.cs ./Tar/InvalidHeaderException.cs ./Tar/TarException.cs ./Tar/TarArchive.cs ./Tar/TarBuffer.cs \
    ./Tar/TarHeader.cs ./Tar/TarEntry.cs ./Tar/TarExtendedHeaderReader.cs ./Tar/TarOutputStream.cs \
    ./GZip/GzipInputStream.cs ./GZip/GZip.cs ./GZip/GZipException.cs ./GZip/GZipConstants.cs ./GZip/GzipOutputStream.cs \
    ./Encryption/ZipAESTransform.cs ./Encryption/ZipAESStream.cs ./Encryption/PkzipClassic.cs \
    ./Checksum/BZip2Crc.cs ./Checksum/Adler32.cs ./Checksum/IChecksum.cs ./Checksum/Crc32.cs \
    ./Checksum/CrcUtilities.cs \
    ./AssemblyInfo.cs \
    -define:NETFRAMEWORK -define:NET45 \
    -keyfile:../../assets/ICSharpCode.SharpZipLib.snk \
    -target:library -out:../../bin/ICSharpCode.SharpZipLib.dll
cd -
%install
mkdir -p %{buildroot}/%{_monogacdir} %{buildroot}/%{_libdir}/pkgconfig
gacutil -i bin/*.dll -f -package %{name} -root %{buildroot}/usr/lib
cat > %{buildroot}/%{_libdir}/pkgconfig/%{name}.pc <<FINISH
prefix=/usr
exec_prefix=\${prefix}
libdir=\${exec_prefix}/lib
Name: sharpziplib
Description: C# Zip, GZip, Tar and BZip2 library for .NET
Version: %{version}
Libs: -r:\${libdir}/mono/sharpziplib/ICSharpCode.SharpZipLib.dll
FINISH
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%files -f %{oreon_filedir}/main.list
%files -n sharpziplib-devel -f %{oreon_filedir}/sharpziplib-devel.list

%changelog

%autochangelog
