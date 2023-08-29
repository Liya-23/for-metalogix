program NML_P;

uses
  Vcl.Forms,
  OnlineEdu_U in 'OnlineEdu_U.pas' {frmOnlineEdu},
  clsNML_U in 'clsNML_U.pas',
  MasterAccount_U in 'MasterAccount_U.pas' {frmMasterAcc},
  Tables_U in 'Tables_U.pas' {dmTables: TDataModule};

{$R *.res}

begin
  Application.Initialize;
  Application.MainFormOnTaskbar := True;
  Application.CreateForm(TfrmOnlineEdu, frmOnlineEdu);
  Application.CreateForm(TfrmMasterAcc, frmMasterAcc);
  Application.CreateForm(TdmTables, dmTables);
  Application.Run;
end.
