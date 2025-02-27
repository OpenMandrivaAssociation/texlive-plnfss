Name:		texlive-plnfss
Version:	15878
Release:	2
Summary:	Font selection for Plain TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/plnfss
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plnfss.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plnfss.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Plnfss is a set of macros to provide easy font access (somewhat
similar to NFSS but with some limitations) with Plain TeX.
Plnfss can automatically make use of PSNFSS fd files, i.e.,
when an Adobe Type 1 is used the relevant fd file will be
loaded automatically. For cmr-like fonts (ec, vnr, csr or plr
fonts), a special format called pfd (plain fd) is required and
must be loaded manually. See ot1cmr.pfd for further
information.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/plain/plnfss/MIKmathf.tex
%{_texmfdistdir}/tex/plain/plnfss/ams.pfd
%{_texmfdistdir}/tex/plain/plnfss/il2cm.pfd
%{_texmfdistdir}/tex/plain/plnfss/il2cmr.pfd
%{_texmfdistdir}/tex/plain/plnfss/ly1lm.pfd
%{_texmfdistdir}/tex/plain/plnfss/ot1cm.pfd
%{_texmfdistdir}/tex/plain/plnfss/ot1cmr.pfd
%{_texmfdistdir}/tex/plain/plnfss/ot4cm.pfd
%{_texmfdistdir}/tex/plain/plnfss/plnfss.tex
%{_texmfdistdir}/tex/plain/plnfss/qxlm.pfd
%{_texmfdistdir}/tex/plain/plnfss/t1lm.pfd
%{_texmfdistdir}/tex/plain/plnfss/t5cm.pfd
%{_texmfdistdir}/tex/plain/plnfss/t5cmr.pfd
%{_texmfdistdir}/tex/plain/plnfss/t5lm.pfd
%{_texmfdistdir}/tex/plain/plnfss/ts1lm.pfd
%doc %{_texmfdistdir}/doc/plain/plnfss/LPPL.txt
%doc %{_texmfdistdir}/doc/plain/plnfss/plnfss.txt
%doc %{_texmfdistdir}/doc/plain/plnfss/test-plnfss.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
